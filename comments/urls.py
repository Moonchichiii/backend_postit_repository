from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'', CommentViewSet, basename='comment')

app_name = 'comments'
urlpatterns = [
    path('', include(router.urls)),
    path('api/posts/<int:post_id>/comments/', views.PostCommentsAPIView.as_view(), name='post-comments'),    
    
]