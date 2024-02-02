from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('users/', include('users.urls', namespace='users')),
    path('api/', include('profiles.urls')),
    path('posts/', include('posts.urls', namespace='posts')),
    
    path('comments/', include('comments.urls', namespace='comments')),
    
    path('likes/', include('likes.urls', namespace='likes')),
    
    path('api/', include('followers.urls', namespace='followers')),
]
