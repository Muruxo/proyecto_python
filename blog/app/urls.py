
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('agregar', views.agregar, name = 'agregar'),
    path('eliminar/<publicacion_id>', views.eliminar, name = 'eliminar'),
    path('actualizar/<publicacion_id>', views.actualizar, name ="actualizar"), 
    path('postular', views.postular, name = 'postular'),
    path('descripcion/<empleo_id>', views.descripcion, name ="descripcion"), 
    path('accounts/', include('allauth.urls')),
    path('DatosPersonales', views.agregarDatosPersonales, name='DatosPersonales'),
   
]
