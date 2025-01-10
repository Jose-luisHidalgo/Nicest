from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('sub/',views.sub),
    path('one/',views.one),
    path('two/',views.two),
    path('three/',views.three),
    path('four/',views.four),
    path('five/',views.five),
    path('top/',views.top),
    path('servers/', views.servers),
    path('api/measurements/', views.obtener_mediciones, name='obtener_mediciones'),
    path('api/devices/', views.get_device_data, name='get_device_data'),
    path('api/devices/0',views.obtener_dispositivos_0),
    path('api/devices/1',views.obtener_dispositivos_1),
    path('api/devices/2',views.obtener_dispositivos_2),
    path('api/devices/3',views.obtener_dispositivos_3),
    path('api/devices/4',views.obtener_dispositivos_4),
    path('api/devices/5',views.obtener_dispositivos_5),
    path('api/devices/6',views.obtener_dispositivos_6),
]