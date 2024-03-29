from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from utils.permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    Filtering, limiting access, search list.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["title"]
    filterset_fields = ["published", "created_at"]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)



    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(
                self.get_serializer(page, many=True).data
            )
        return Response(self.get_serializer(queryset, many=True).data)         


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




    def liked_post(self, request):
        liked_post = Post.objects.filter(published=True).order_by('-likes_count').first()

        if liked_post:
            serializer = PostSerializer(liked_post)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
