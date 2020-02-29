from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        print(usuario)
        print(senha)
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario e senha inválido. Favor tentar novamente')
    return redirect('/login/')

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')
