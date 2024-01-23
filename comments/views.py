from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        
        serializer.save(profile=self.request.user.profile)
