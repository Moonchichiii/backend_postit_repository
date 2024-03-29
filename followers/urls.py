from django.urls import path
from .views import FollowerList, FollowerDetail

app_name = 'followers'

urlpatterns = [
    path('followers/', FollowerList.as_view(), name='follower-list'),
    path('<int:pk>/', FollowerDetail.as_view(), name='follower-detail'),
]
