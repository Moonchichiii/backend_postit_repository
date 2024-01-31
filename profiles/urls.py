from django.urls import path
from .views import ProfileList, ProfileDetail

app_name = 'profiles'



app_name = 'profiles'
urlpatterns = [  
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),    
]
    