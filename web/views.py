from django.shortcuts import render
from django.shortcuts import render
from .models import Persona

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def portafolio(request):
    return render(request, 'portafolio.html')

def contacto(request):
    return render(request, 'contacto.html')

def about(request):

    persona_info = Persona.objects.first()
    return render(request, 'about.html', {'persona': persona_info})