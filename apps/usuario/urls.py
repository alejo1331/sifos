"""SIFO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from apps.usuario.views import perfil, validate_email, recover_password

urlpatterns = [
    path('perfil/', perfil, name="usuario_perfil"),
    path('validate_email/', validate_email, name='validate_email'),
    path('send_email/', recover_password, name='send_email'),
]
