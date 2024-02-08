from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile
from .serializers import ProfileSerializer



from .models import Profile

# Create your views here.

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update your own profile.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile


class ProfileList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
     
        posts_count=Count('posts', distinct=True),
     
        followers_count=Count('followers', distinct=True),
     
     
        following_count=Count('user__following', distinct=True),
    ).order_by('-created_at')
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    
    filterset_fields = ['user__following__followed_profile', 'followers__user']
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'created_at',
    ]