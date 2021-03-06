"""SIFO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from apps.terreno.views import index, registro, registro_poligono, eliminar_terreno, edicion, updpoligono, sowing_points_pending, update_sowing

urlpatterns = [
    path('seguimiento', index, name='terreno_seguimiento'),
    path('registro', registro, name='terreno_registro'),
    path('edicion/<int:terreno_id>/', edicion, name='terreno_edicion'),
    path('registrar_poligono', registro_poligono, name='terreno_registrar_poligono'),
    path('eliminar_terreno', eliminar_terreno, name='eliminar_terreno'),
    path('updpoligono', updpoligono, name='updpoligono'),
    url(r'^sowing_pending', sowing_points_pending),
    url(r'^update_sowing', update_sowing),
]