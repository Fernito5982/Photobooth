from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.contrib import messages, auth
from .models import Perfil, Post,LikePost,FollowersCount
from itertools import chain
import random

#Prueba
# Create your views here.
@login_required(login_url='signin')
def index(request):
    
    # Obtienes datos del usuario en sesion
    user_object = User.objects.get(username = request.user.username)
    
    user_perfil = Perfil.objects.get(user = user_object)

    usuarios = Perfil.objects.all()


    # Filtro para solo mostrar publicaciones de usuarios seguidos
    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower = request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_lists = list(chain(*feed))


    # Funciones de sugerencia de seguidores
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    
    new_suggestion_list = [x for x in list(all_users) if(x not in list(user_following_all))]

    current_user = User.objects.filter(username = request.user.username)
    final_suggestion_list = [x for x in list(new_suggestion_list) if(x not in list(current_user))] 

    random.shuffle(final_suggestion_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestion_list:
        username_profile.append(users.id)
    
    for ids in username_profile:
        profile_lists = Perfil.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)
    
    suggestions_usernames_profile_list = list(chain(*username_profile_list))

    return render(request,'index.html', {'user_perfil': user_perfil, 'posts':feed_lists, 'usuarios':usuarios,'suggestions_usernames_profile_list':suggestions_usernames_profile_list[:4]})

def likes_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id = post_id, username = username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id = post_id, username = username)
        new_like.save()
        post.number_likes = post.number_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.number_likes = post.number_likes-1
        post.save()
        return redirect('/')

@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('imagen_cargada')
        caption = request.POST['caption']
        print(image)
        
        new_post = Post.objects.create(user = user, image = image, caption = caption) 
        new_post.save()
        print("Se almaceno")
        return redirect('/')
    else:
        return redirect('/')

def signup(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        username = request.POST['usuario']
        email = request.POST['email']
        password = request.POST['password']
        image = request.FILES.get('Avatar')

        if password == request.POST['confirm_password']:
           
           if User.objects.filter(email = email).exists():
               messages.info(request,'Ya existe este correo')
               return redirect('signup')
           
           elif User.objects.filter(username = username).exists():
               messages.info(request,'Ya existe este usuario')
               return redirect('signup') 
           
           else:
               user = User.objects.create_superuser(
                   username= username,
                   email= email,
                   password=password,
                   first_name = nombre,
                   last_name = apellido,
                   
                )
               user.save()
               user_model = User.objects.get(username=username)
               

               new_perfil = Perfil.objects.create(
                   user=user_model,
                   id_user=user_model.id,
                   profileimg = image,
                   )
                 

               new_perfil.save()          

               return redirect('signin')
            
        else:
            messages.info(request,'Contraseña Invalida')
            return redirect('signup')
            
        
    else:
        return render(request,'signup.html')

def signin(request):
    
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username = username, password = password)
       
       

       if user is not None:
            auth.login(request,user)
            return redirect('/')
       else:
            messages.info(request,'Usuario no encontrado')
            return redirect('signin')
    else:
        return render(request,'signin.html')    
    
def logout(request):
    auth.logout(request)
    return redirect('signin')

def profile(request,pk):
    user_object = User.objects.get(username=pk)
    user_profile = Perfil.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk
    if FollowersCount.objects.filter(follower=follower,user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'
    
    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }

    return render(request,'profile.html',context)

@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower,user=user).first():
            delete_follower = FollowersCount.objects.get(follower = follower,user = user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower = follower,user = user)
            new_follower.save()
            return redirect('/profile/'+user)

def search(request):

    user_object = User.objects.get(username = request.user.username)
    user_profile = Perfil.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username) 

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_list = Perfil.objects.filter(id_user = ids)
            username_profile_list.append(profile_list)
        
        username_profile_list = list(chain(*username_profile_list))


    return render(request,'search.html',{'user_profile':user_profile, 'username_profile_list':username_profile_list})