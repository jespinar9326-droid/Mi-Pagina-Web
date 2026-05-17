from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):

    list_display = ('nombres', 'apellidos', 'titulo_academico', 'correo_electronico')