from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth

# Create your views here.
@login_required(login_url='signin')
def index(request):
    return render(request,'index.html')

def signup(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        username = request.POST['usuario']
        email = request.POST['email']
        password = request.POST['password']
        anio_nacimiento = request.POST['anio_nacimiento']

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
                   
                )
               user.save()

               
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

