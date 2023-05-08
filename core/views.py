from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.contrib import messages, auth
from .models import Perfil, Post,LikePost

#Prueba
# Create your views here.
@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username = request.user.username)
    
    user_perfil = Perfil.objects.get(user = user_object)
    
    posts = Post.objects.all()
    usuarios = Perfil.objects.all()

    return render(request,'index.html', {'user_perfil': user_perfil, 'posts':posts, 'usuarios':usuarios})

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

