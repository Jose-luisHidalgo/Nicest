from rest_framework import serializers
from .models import Institucion, EventoAcademico, Feriado,Tipo

class Institucion_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Institucion
        fields=('nombre',)
class EventoAcademico_Serializer(serializers.ModelSerializer):
    class Meta:
        model=EventoAcademico
        fields='__all__'
class Feriado_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Feriado
        fields='__all__'

class Tipo_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Tipo
        fields='__all__'