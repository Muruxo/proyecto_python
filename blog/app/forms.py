from django import forms
from django.utils import timezone
from django.forms import ModelForm
from django.shortcuts import render

from .models import Empleo, Publicacion, Postulante, Detallepostulante

MODALIDAD_EMPLEO_CHOICES = ["Activado", "Desactivado", "Pendiente"]

class EmpleoForm(ModelForm):
    class Meta: 
        model = Empleo
        fields = '__all__'
        labels = {
            'nombre_empleo': 'Empleo', 
            'descripcion_empleo' : 'Descripción',
            'fecha_empleo': 'Fecha de Publicación',
            'area_empleo': 'Area del Empleo',
            'modalidad_empleo': 'Modalidad de Trabajo',
            'tiempo_empleo': 'Tiempo de contrato',
            'id_ciudad_fk': 'Ciudad',
            
        }
        widgets = {
            'nombre_empleo': forms.TextInput(attrs = {'class': 'form-control'}),
            'descripcion_empleo': forms.Textarea(attrs = {'class': 'form-control'}),
            'fecha_empleo':forms.DateInput(attrs={'class': 'form-control', 'display':'center' }),
            'area_empleo': forms.TextInput(attrs = {'class': 'form-control'}),
            'modalidad_empleo': forms.TextInput(attrs = {'class': 'form-control'}),
            'tiempo_empleo':forms.TextInput(attrs= {'type': 'number', 'class': 'form-control'}),
            'id_ciudad_fk':forms.TextInput(attrs = {'class': 'form-control'}),
        }
        
class PublicacionForm(ModelForm):
    class Meta: 
        model = Publicacion
        fields = '__all__'
        labels = {
            'titulo': 'Empleo', 
            'descripcion' : 'Descripción',
            'email': 'Email',
        }
        widgets = {
            'titulo': forms.TextInput(attrs = {'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
        }
        

class DatosPersonales(forms.ModelForm):
    class Meta: 
        genero = {'':'','M':'Masculino', 'F':'Femenino'}
        model = Postulante
        fields = ['nombre_postulante','apellido_postulante','email_postulante','telefono_postulante','genero_postulante','edad_postulante','ciudad_postulante','direccion_postulante']
        labels = {  
            'nombre_postulante': 'Nombres',
            'apellido_postulante': 'Apellidos', 
            'email_postulante': 'Email', 
            'telefono_postulante': 'Teléfono', 
            'genero_postulante': 'Género', 
            'edad_postulante': 'Edad', 
            'ciudad_postulante': 'Ciudad', 
            'direccion_postulante': 'Dirección'
        }
        widgets = { 
             'nombre_postulante': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellido_postulante': forms.TextInput(attrs = {'class': 'form-control'}),
            'email_postulante': forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono_postulante': forms.NumberInput(attrs = {'class': 'form-control'}),
            'genero_postulante' : forms.Select(choices=genero.items()),
            'edad_postulante':  forms.NumberInput(attrs = {'class': 'form-control'}), 
            'ciudad_postulante': forms.TextInput(attrs = {'class': 'form-control'}),
            'direccion_postulante': forms.TextInput(attrs = {'class': 'form-control'}),
        }

