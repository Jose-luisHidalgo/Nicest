from django.contrib import admin
from .models import Institucion, EventoAcademico, Feriado,Tipo
# Register your models here.
admin.site.register(Institucion)
admin.site.register(EventoAcademico)
admin.site.register(Feriado)
admin.site.register(Tipo)