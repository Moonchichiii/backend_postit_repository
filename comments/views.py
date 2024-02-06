from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post

class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling comments.
    Ensures that only authenticated users can interact with comments.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(profile=self.request.user.profile, post=post)

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post_id=post_id)