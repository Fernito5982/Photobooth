from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup',views.signup, name = 'signup'),
    path('signin',views.signin, name = 'signin'),
    path('logout',views.logout, name = 'logout'),
    path('likes_post',views.likes_post, name = 'likes_post'),
    path('upload',views.upload, name = 'upload')
]
