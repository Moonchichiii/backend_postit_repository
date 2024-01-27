from django.urls import path
from .views import UserRegistrationView, TokenObtainWithUserIdView, DeleteAccountView, ChangePasswordView
from rest_framework_simplejwt.views import TokenRefreshView 

app_name = 'users'
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('token/', TokenObtainWithUserIdView.as_view(), name='token_obtain_with_user_id'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete-account'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]