from django.urls import path
from .views import ProfileList, ProfileDetail, PopularProfileList

app_name = 'profiles'
urlpatterns = [
    path('', ProfileList.as_view(), name='profile-list'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('popular/', PopularProfileList.as_view(), name='popular-profiles'),  
]

    