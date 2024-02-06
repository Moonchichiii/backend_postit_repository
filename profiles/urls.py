from django.urls import path
from .views import ProfileList, ProfileDetail, CurrentUserProfileView

app_name = 'profiles'

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('profile/', CurrentUserProfileView.as_view(), name='current-user-profile'),
]