from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios_view, name='servicios'),
    path('citas/', views.lista_citas, name='citas'),
    path('contacto/', views.contacto_view, name='contacto'),
]