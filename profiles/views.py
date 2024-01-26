from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from utils.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from profiles.models import Profile
from rest_framework.views import APIView


class ProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing profiles.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProfileUpdateView(APIView):
    """
    APIView for updating a profile.
    """
    permission_classes = [IsOwnerOrReadOnly]

    def post(self, request):
        """
        Update the profile with the provided image URL.
        """
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        profile_image_url = request.data.get("image_url")

        if profile_image_url:
            profile.profile_image = profile_image_url
            profile.save()

        return Response({"message": "Profile updated"})
