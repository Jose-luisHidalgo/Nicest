from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('Institucion',views.Institucion_ViewSets)
router.register('EventoAcademico',views.EventoAcademico_ViewSets)
router.register('Feriado', views.Feriado_ViewSets)
router.register('Tipo', views.Tipo_ViewSets)

urlpatterns = [
    path('', include(router.urls)),
]