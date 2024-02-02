from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Follower
from .serializers import FollowerSerializer


# Create your views here.

class FollowerList(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self): 
     return Follower.objects.filter(followed=self.request.user)

    def perform_create(self, serializer):        
        serializer.save(profile=self.request.user)
        
        
        

class FollowerDetail(generics.RetrieveDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]