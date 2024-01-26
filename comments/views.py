from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post

# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling comments
    """
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(profile=self.request.user.profile, post=post)

class PostCommentsAPIView(ListAPIView):
    """
    listing comments. 
    """
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_pk'] 
        return Comment.objects.filter(post__id=post_id)
    

    
    def edit_comment(self, request, pk=None):
        comment = self.get_object()
        serializer = CommentSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_comment(self, request, pk=None):
        comment = self.get_object()
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)