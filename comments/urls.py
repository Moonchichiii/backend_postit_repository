from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'comments'
router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]