from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import PostViewSet
from comments.views import CommentViewSet
from likes.views import LikeViewSet

# router for posts
router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

# routes for comments

comments_router = routers.NestedSimpleRouter(router, r'', lookup='post')

comments_router.register(r'comments', CommentViewSet, basename='post-comments')


likes_router = routers.NestedSimpleRouter(router, r'', lookup='post')

likes_router.register(r'likes', LikeViewSet, basename='post-likes')


app_name = 'posts'
urlpatterns = [
    path('', include(router.urls)),
    path('', include(comments_router.urls)),
    path('', include(likes_router.urls)),
]
