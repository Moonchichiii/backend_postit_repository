from django.db.models import Count
from rest_framework import generics
from rest_framework.response import Response
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



class CurrentUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = ProfileSerializer(request.user.profile)
        return Response(serializer.data)