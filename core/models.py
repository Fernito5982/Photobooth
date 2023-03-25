from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    id_usuario = models.IntegerField()
    bio = models.TextField(blank = True)
    profileimg = models.ImageField(upload_to = 'profile_images', default = 'https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg')
    
    def __str__(self):
        return self.usuario.get_username
    
class Post(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    usuario = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default = datetime.now)
    number_likes = models.IntegerField(default = 0)

    def __str__(self):
        return self.usuario 

