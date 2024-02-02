from django.db.models import Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django.db.models import Exists, OuterRef
from followers.models import Follower
from .models import Profile
from .serializers import ProfileSerializer

from utils.permissions import IsOwnerOrReadOnly


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update your own profile.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        return self.request.user.profile



class ProfileList(generics.ListAPIView):
    """
    List profiles of users you are following and your own profile.
    """
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    permission_classes = [IsAuthenticated]
    filterset_fields = [
        'user__following__followed__profile',
        'user__followed__profile',
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            
            return Profile.objects.annotate(
                is_following=Exists(
                    Follower.objects.filter(
                        profile=user.profile,
                        followed=OuterRef('user')
                    )
                )
            ).order_by('-created_at')
        return Profile.objects.none()



class PopularProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.annotate(
            followers_count=Count('followed')
        ).order_by('-followers_count')

