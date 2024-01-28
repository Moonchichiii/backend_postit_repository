from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ProfileSerializer
from profiles.models import Profile

from utils.permissions import IsOwnerOrReadOnly

class ProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing profiles.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
         
        profile = self.get_object()
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
