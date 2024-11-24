from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Institucion_Serializer,EventoAcademico_Serializer,Feriado_Serializer, Tipo_Serializer
from .models import Institucion,EventoAcademico,Feriado, Tipo
# Create your views here.

class Institucion_ViewSets(viewsets.ModelViewSet):
    queryset=Institucion.objects.all()
    serializer_class=Institucion_Serializer

class EventoAcademico_ViewSets(viewsets.ModelViewSet):
    queryset=EventoAcademico.objects.all()
    serializer_class=EventoAcademico_Serializer

class Feriado_ViewSets(viewsets.ModelViewSet):
    queryset=Feriado.objects.all()
    serializer_class=Feriado_Serializer

class Tipo_ViewSets(viewsets.ModelViewSet):
    queryset=Tipo.objects.all()
    serializer_class=Tipo_Serializer
    
def start(request):
    lista_eventos = EventoAcademico.objects.all()
    lista_feriados = Feriado.objects.all()
    return render(request, 'start.html', {
        'Lista_eventos' : lista_eventos,
        'Lista_feriados' : lista_feriados,
    })

