from rest_framework import viewsets

from profiles.models import Profile

from utils.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing user profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
