
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios_view, name='servicios'),
    path('citas/', views.lista_citas, name='citas'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('crea/', views.crea_Cita, name="crea_Cita"),
    path('editar/<int:pk>/', views.editar_cita, name="editar_cita"),
    path('eliminar/<int:pk>/', views.eliminar_cita, name="eliminar_cita"),


    
]