from django.contrib import admin
from .models import Perfil, Post,LikePost,FollowersCount

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)

