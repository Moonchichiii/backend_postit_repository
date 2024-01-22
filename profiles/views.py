from rest_framework import viewsets
from utils.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from .models import Profile
import logging


# Create your views here.

logger = logging.getLogger(__name__)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        logger.info(f"Creating profile with data: {serializer.validated_data}")
        serializer.save(user=self.request.user)

