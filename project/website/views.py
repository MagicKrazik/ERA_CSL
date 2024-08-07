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

def pictures_site(request):
    return render(request, 'pictures_site.html')


#def upload_pictures(request):
#    clients = Client.objects.all()  # Assuming you have a Client model
#    context = {
#        'clients': clients,
#    }
#    return render(request, 'pictures_site.html', context)