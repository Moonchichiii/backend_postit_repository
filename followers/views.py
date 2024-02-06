from rest_framework import generics, response, status
from .models import Follower
from .serializers import FollowerSerializer
from utils.permissions import IsOwnerOrReadOnly

class FollowerList(generics.ListCreateAPIView):
    """
    API view for listing and creating followers.
    """
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        followed_user = serializer.validated_data.get('followed_user')
        if self.request.user == followed_user:
            raise serializers.ValidationError("You cannot follow yourself.")
        if Follower.objects.filter(user=self.request.user, followed_user=followed_user).exists():
            return response.Response(
                {"detail": "You are already following this user."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(user=self.request.user)


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