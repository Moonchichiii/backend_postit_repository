from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post
from .serializers import PostSerializer
from utils.permissions import IsAuthenticatedOrReadOnlyForPost


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    """
    filtering, limiting access, search list 
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForPost]
    
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content', 'user__username']
    filterset_fields = ['published', 'user__username', 'created_at']

    
    def perform_create(self, serializer):
        # creating a new post                
        serializer.save(user=self.request.user)
