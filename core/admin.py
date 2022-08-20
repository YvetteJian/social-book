from django.contrib import admin

# Register your models here.
from .models import Profile, Post,LikePost,FollowersCount

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
