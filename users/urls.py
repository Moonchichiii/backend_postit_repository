from django.urls import path
from .views import UserRegistrationView, UserLoginView, ChangePasswordView
from rest_framework_simplejwt.views import TokenRefreshView 

app_name = 'users'
urlpatterns = [
    
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('login/', UserLoginView.as_view(), name='user-login'),
    
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
