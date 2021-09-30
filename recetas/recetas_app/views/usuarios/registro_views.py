from  django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse

def registro(request):
    context={}
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_exist = User.objects.filter(username = username).exists()
        if user_exist:
            error="El usuario que intenta registrar ya se encuentra registrado"
            context['error']=error
            context['name']=name
            context['lastname']=lastname
            context['email']=email
            context['username']=username
            
        else:
            user = User.objects.create_user(username,email,password, first_name=name, last_name=lastname)
            url = "{}?greetings=true".format(reverse('login'))
            return redirect(url)
    else:
        print("GET")

    return render(request,'usuarios/registro.html', context)

def login(request):
    context={}
    if request.method=="GET":
        greetings = request.GET.get('greetings')
        if greetings=="true":
            context['response']="Su usuario se ha creado correctamente, ya puede iniciar sesión"
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse('home'))
        else:
            error="Usuario o contraseña inválida"
            context['error']=error

    return render(request,'usuarios/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect(reverse('home'))