
import logging
from rest_framework import generics, response, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Follower
from .serializers import FollowerSerializer


logger = logging.getLogger(__name__)


class FollowerList(generics.ListCreateAPIView):
    """
    API view for listing and creating followers.
    """
    queryset = Follower.objects.all().order_by('id')
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        logger.debug("Request data: %s", serializer.validated_data)
        followed_profile = serializer.validated_data.get('followed_profile')
        logger.debug("Request data: %s", serializer.validated_data.get)
        if self.request.user.profile == followed_profile:
            raise serializers.ValidationError("You cannot follow yourself.")
        if Follower.objects.filter(user=self.request.user, followed_profile=followed_profile).exists():            
            return response.Response(
                {"detail": "You are already following this user."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(user=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a follower.
    """
    permission_classes = [IsAuthenticated]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            raise PermissionDenied("You don't have permission to delete this follower! ")
        return super().destroy(request, *args, **kwargs)