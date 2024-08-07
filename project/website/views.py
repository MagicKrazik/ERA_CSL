from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def cotizaciones_view(request):
    return render(request, 'cotizaciones.html')

@login_required
def pictures_site(request):
    return render(request, 'pictures_site.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def login_operadores(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login_operadores.html')

def logout_view(request):
    logout(request)
    return redirect('home')