from django.shortcuts import render
from .models import Cliente

def inicio(request):
    return render(request, 'spaap/index.html')

def servicios_view(request):
    # Aquí puedes mostrar un catálogo estático o dinámico de los servicios del spa
    return render(request, 'spaap/servicios.html')

def lista_citas(request):
    # Esta es la vista donde se ven las citas agendadas que tenías antes
    servicios = Cliente.objects.all()
    contexto = {'servicios': servicios}
    return render(request, 'spaap/citas.html', contexto)

def contacto_view(request):
    return render(request, 'spaap/contacto.html')