from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Like

# Register your models here.

class LikeAdmin(admin.ModelAdmin):

    search_fields = ['like', 'post', 'created_at'] 


    
admin.site.register(Like, LikeAdmin)