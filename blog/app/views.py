from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Publicacion, Empleo, Postulante, Experiencia, Detallepostulante
from  .forms import PublicacionForm, EmpleoForm, DatosPersonalesForm, ExperienciaForm, DatosAdicionalesForm, EducacionForm

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
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Informacion agregada con éxito')
        return redirect(agregarDatosAdicionales) 

    return render(request, 'app/DatosPersonales.html', {'form':DatosPersonalesForm})


@login_required    
def agregarDatosAdicionales(request): 
    if request.POST: 
        ExperienciaForm1 = ExperienciaForm(request.POST)
        DatosAdicionalesForm1 = DatosAdicionalesForm(request.POST)
        if ExperienciaForm1.is_valid() and DatosAdicionalesForm1.is_valid():
            ExperienciaForm1.save()
            DatosAdicionalesForm1.save()
        messages.success(request, 'Informacion agregada con éxito')
        return redirect(agregarDatosEducacion)  

    return render(request, 'app/DatosAd.html', {'form1':ExperienciaForm, 'form2': DatosAdicionalesForm})


@login_required    
def agregarDatosEducacion(request): 
    if request.POST: 
        form = EducacionForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Informacion agregada con éxito')
        return redirect(index)  

    return render(request, 'app/DatosEducacion.html', {'form':EducacionForm})