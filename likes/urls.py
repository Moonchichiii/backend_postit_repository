from django.urls import path, include
from rest_framework_nested import routers
from .views import LikeViewSet
from posts.views import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

likes_router = routers.NestedSimpleRouter(router, 'posts', lookup='post')
likes_router.register('likes', LikeViewSet, basename='post-likes')


app_name = 'likes'
urlpatterns = [
    path('', include(router.urls)),
    path('', include(likes_router.urls)),
]