from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import OperatorCreationForm
from django.contrib.auth import authenticate, login, logout


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
            return redirect('pictures_site')
        else:
            messages.error(request, 'Nombre de usuario o contraseña inválidos')
    return render(request, 'login_operadores.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def create_operator(request):
    if request.method == 'POST':
        form = OperatorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Operador creado exitosamente.')
            return redirect('operator_list')  # You'll need to create this view
    else:
        form = OperatorCreationForm()
    return render(request, 'create_operator.html', {'form': form})

@user_passes_test(is_admin)
def operator_list(request):
    operators = User.objects.filter(is_staff=False)
    return render(request, 'operator_list.html', {'operators': operators})