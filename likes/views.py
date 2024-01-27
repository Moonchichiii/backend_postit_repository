from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Like
from .serializers import LikeSerializer
from posts.models import Post

class LikeViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing likes.
    """
    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(user=self.request.user, post=post, profile=self.request.user.profile)
