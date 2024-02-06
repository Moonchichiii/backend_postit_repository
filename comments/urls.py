from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet


router = DefaultRouter()
router.register(r'', CommentViewSet, basename='post-comment')

app_name = 'comments'
urlpatterns = [
    path('', include(router.urls)),
]
