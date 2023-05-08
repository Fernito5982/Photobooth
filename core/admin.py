from django.contrib import admin
from .models import Perfil, Post,LikePost

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Post)
admin.site.register(LikePost)

