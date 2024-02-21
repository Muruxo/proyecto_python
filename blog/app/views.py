from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Publicacion, Empleo, Postulante
from  .forms import PublicacionForm, EmpleoForm, DatosPersonales

def actualizar(request, publicacion_id): 
    publicacion = Empleo.objects.get(pk = publicacion_id)
    form = EmpleoForm(request.POST or None, instance = publicacion)
    if form.is_valid(): 
        form.save()
        messages.success(request, 'Publicación Actualizada')
        return redirect(home)  
    return render(request, 'app/actualizar.html', {'publicacion':publicacion, 'form': form})
    
def eliminar(request, publicacion_id):
    publicacion = Empleo.objects.get(pk = publicacion_id)
    publicacion.delete()
    messages.success(request, 'Publicación Eliminada')
    return redirect(home)  

@login_required    
def agregar(request): 
    if request.POST: 
        form = EmpleoForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Publicacion Añadida')
        return redirect(home)  

    return render(request, 'app/agregar.html', {'form':EmpleoForm})

def home(request): 
    empleos = Empleo.objects.all()
    return render(request, 'app/home.html', {'empleos': empleos})

def index(request):
    empleos = Empleo.objects.all()
    return render(request, 'app/index.html', {'empleos': empleos})

def postular(request, empleo_id, postulante_id): 
    # publicacion = Empleo.objects.get(pk = publicacion_id)
    # form = EmpleoForm(request.POST or None, instance = publicacion)
    # if request.POST: 
    #     form = EmpleoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     messages.success(request, 'Postulación Exitosa')
        return redirect()  
    
def descripcion(request, empleo_id): 
    # Query del perro, un perro con el codigo
    empleo = Empleo.objects.get(pk = empleo_id)
    
    # creo un diccionario con el objeto
    contenido = {
        'empleo' : empleo
    }
    template = "app/descripcion.html"
    return render(request, template, contenido)


#FORM DATOS PERSONALES POSTULANTE

@login_required    
def agregarDatosPersonales(request): 
    if request.POST: 
        form = DatosPersonales(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Informacion agregada con éxito')
        return redirect(home)  

    return render(request, 'app/DatosPersonales.html', {'form':DatosPersonales})