from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CitaForm
from .models import Cliente, Cita

def inicio(request):
    return render(request, 'spaap/index.html')

def servicios_view(request):
    # Aquí puedes mostrar un catálogo estático o dinámico de los servicios del spa
    return render(request, 'spaap/servicios.html')

def lista_citas(request):
    # Cambiamos Cliente por Cita para traer todas las citas agendadas
    citas = Cita.objects.all()
    contexto = {'citas': citas}
    return render(request, 'spaap/citas.html', contexto)

def contacto_view(request):
    return render(request, 'spaap/contacto.html')

def crea_Cita(request):
    form = CitaForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Cita registrada correctamente')
        return redirect('crea_Cita') 
        
    return render(request, 'spaap/boton.html', {'form': form}) 

def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    
    form = CitaForm(request.POST or None, instance=cita)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Editado de manera correcta')
        return redirect('citas')  # O la ruta que lista tus citas
        
    nombre_cliente = f"{cita.cliente_rel.nombre}" if cita.cliente_rel else "Sin cliente"
    
    return render(request, 'spaap/editar.html', {
        'form': form,
        'titulo': f'Editar Cita de {nombre_cliente}'
    })



def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('citas')
    # Cambia 'spaap/eliminar_cita.html' por 'spaap/eliminar.html'
    return render(request, 'spaap/eliminar.html', {'cita': cita})