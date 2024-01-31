from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters

from followers.models import Follower

from .models import Profile
from .serializers import ProfileSerializer
from utils.permissions import IsOwnerOrReadOnly


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from followers.models import Follower
from .models import Profile
from .serializers import ProfileSerializer
from utils.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List profiles of users you are following and your own profile.
    """
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'user__following__followed__profile',
        'user__followed__profile',
    ]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:

            following_profiles = Follower.objects.filter(profile=user).values_list('followed__profile', flat=True)
            return Profile.objects.filter(pk__in=following_profiles).order_by('-created_at') | Profile.objects.filter(pk=user.profile.pk)
        else:
            return Profile.objects.none()

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update your own profile.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:

            return Profile.objects.filter(pk=user.profile.pk)
        else:
            return Profile.objects.none()
