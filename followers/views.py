from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from .models import Follower
from .serializers import FollowerSerializer
from utils.permissions import IsOwnerOrReadOnly

class FollowerList(generics.ListCreateAPIView):
    """
    API view for listing and creating followers.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        target_user_id = serializer.validated_data.get('followed_user').id
        if target_user_id == self.request.user.id:
            raise serializers.ValidationError("You cannot follow yourself.")
        if Follower.objects.filter(profile__user=self.request.user, followed_user=target_user_id).exists():
            return Response(
                {"detail": "You are already following this user."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(profile=self.request.user.profile)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a follower.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context