from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cotizaciones_view(request):
    return render(request, 'cotizaciones.html')

def login_operadores(request):
    return render(request, 'login_operadores.html')

def login_clientes(request):
    return render(request, 'login_clientes.html')