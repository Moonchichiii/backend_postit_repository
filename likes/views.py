from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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
        post_id = self.kwargs['post_pk']        
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(profile=self.request.user.profile, post=post)
        
        
        
class LikeList(generics.ListCreateAPIView):
    """
    List likes for a post
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    
    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Like.objects.filter(post=post_id)

    # Get the id of the post that is being liked

    def perform_create(self, serializer):
        
        post_id = self.kwargs['post_pk']
        
        post = get_object_or_404(Post, pk=post_id)

        # Check if the user already liked the post before
        serializer.save(profile=self.request.user.profile, post=post)

        # Increment the likes_count of the post
        post.likes_count += 1
        post.save()

        # increment the total number of likes each user has received
        profile = self.request.user.profile
        profile.total_likes_received += 1
        profile.save()


    # getting the id of the post being liked. 

    def create(self, request, *args, **kwargs):
        
        post_id = self.kwargs['post_pk']
        try:
            
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


        #  checkand save the like
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, post=post)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    