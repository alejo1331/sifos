# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
from apps.terreno.models import Poligono, Siembra, PuntoSiembra
from apps.general.models import Municipio, TipoPatron
from apps.usuario.views import get_user_donor_by_donation, send_email

import json
import os


def index(request):
    obj = Poligono.objects.filter(usuario=request.user)

    for abc in Poligono.objects.raw('''select tp.id,
    (select count(distinct(tps.especie_id)) from terreno_punto_siembra tps where tps.poligono_id=tp.id) as especie,
    (select SUM(fd.valor)from terreno_siembra ts, financiacion_donacion fd, terreno_punto_siembra tps
    where ts.donacion_id=fd.id and ts.punto_siembra_id=tps.id and tps.poligono_id=tp.id) as valor_donacion,
    (select COUNT(fd.donador_id) from terreno_siembra ts, financiacion_donacion fd, terreno_punto_siembra tps
    where ts.donacion_id=fd.id and ts.punto_siembra_id=tps.id and tps.poligono_id=tp.id) as cant_donadores
    from terreno_poligono tp'''):
        obj_nombre = abc.nombre
        obj_coordenadas_puntos = abc.coordenadas_puntos
        obj_area = abc.area
        obj_perimetro = abc.perimetro
        obj_tipo_patron = abc.tipo_patron
        obj_municipio = abc.municipio
        obj_fecha = abc.fecha
        obj_especie = abc.especie
        obj_valor_donacion = abc.valor_donacion
        obj_cant_donadores = abc.cant_donadores

    context = {}
    if obj.exists():
        context = {
            "obj": obj,
            "obj_nombre": obj_nombre,
            "obj_coordenadas_puntos": obj_coordenadas_puntos,
            "obj_area": obj_area,
            "obj_perimetro": obj_perimetro,
            "obj_tipo_patron": obj_tipo_patron,
            "obj_municipio": obj_municipio,
            "obj_fecha": obj_fecha,
            "obj_especie": obj_especie,
            "obj_valor_donacion": obj_valor_donacion,
            "obj_cant_donadores": obj_cant_donadores
        }

    return render(request, "terreno/index.html", context)


def registro(request):
    list_tipo = TipoPatron.objects.all()
    context = {
        "list_tipo": list_tipo
    }

    return render(request, "terreno/registrar.html", context)


def edicion(request, terreno_id):
    list_tipo = TipoPatron.objects.all()
    det_terreno = Poligono.objects.get(id=terreno_id)

    jsonData = json.loads(det_terreno.coordenadas_puntos)
    puntos = json.dumps(jsonData).replace("\'", "\"")

    context = {
        "list_tipo": list_tipo,
        "nombre": det_terreno.nombre,
        "area": det_terreno.area,
        "perimetro": det_terreno.perimetro,
        "puntos": puntos

    }
    return render(request, "terreno/editar.html", context)


def registro_poligono(request):
    data = {
        'error': "no",
        'message': "Success."
    }
    try:
        m = Municipio.objects.get(nombre=request.GET.get('municipio', None))
        p = Poligono(nombre=request.GET.get('name', None), coordenadas_puntos=request.GET.get('points', None),
                     area=request.GET.get('area', None),
                     perimetro=request.GET.get('perimeter', None), usuario=request.user, municipio_id=m.id,
                     tipo_patron_id=request.GET.get('siembra', None))
        p.save()
    except Exception as e:
        data = {
            'error': "si",
            'message': "Error."
        }
    return JsonResponse(data)


def eliminar_terreno(request):
    pk = request.POST.get('id')
    identificador = Poligono.objects.get(id=pk)
    identificador.delete()
    response = {}
    return JsonResponse(response)


def updpoligono(request):
    data = {
        'error': "si",
        'message': "Success."
    }
    try:
        m = Municipio.objects.get(nombre=request.POST.get('municipio', None))
        obj = Poligono.objects.get(d=request.POST.get('id', None))
        obj.nombre = request.POST.get('name', None)
        obj.coordenadas_puntos = request.POST.get('points', None)
        obj.area = request.POST.get('area', None)
        obj.perimetro = request.POST.get('perimeter', None)
        obj.tipo_patron_id = request.POST.get('siembra', None)
        obj.usuario = request.user
        obj.municipio_id = m.id
        obj.save()
    except Exception as e:
        data1 = {
            'error': "no",
            'message': "Error."
        }

    return JsonResponse(data)


@csrf_exempt
def sowing_points_pending(request):
    post_data = json.loads(request.body)
    robot_id = post_data['robot_id']

    sowing_points = PuntoSiembra.objects.all().filter(
        siembra__temperatura__isnull=True,
        siembra__humedad__isnull=True,
        siembra__altitud__isnull=True,
        siembra__ph__isnull=True,
        siembra__url_video__isnull=True,
        siembra__robot_id__exact=robot_id
    ).values()

    return JsonResponse(list(sowing_points), safe=False)


@csrf_exempt
def update_sowing(request):
    response = {'success': True}
    post_data = json.loads(request.body)
    sowing_point_id = post_data['sowing_point_id']
    sowing = Siembra.objects.get(punto_siembra=sowing_point_id)
    sowing.temperatura = post_data['temperature']
    sowing.humedad = post_data['humidity']
    sowing.altitud = post_data['altitude']
    sowing.ph = post_data['ph']
    sowing.url_video = post_data['url_video']

    try:
        sowing.save()
        user_donator = get_user_donor_by_donation(sowing.donacion.id)
        send_email_user(user_donator, sowing)
    except ValueError:
        response = {'success': False}

    return JsonResponse(response, safe=False)


def send_email_user(user_donator, sowing):
    subject = 'Siembra de plantula'
    message = 'Querido ' + user_donator.nombre + 'gracias a tu donación hemos sembrado vida <a href="' + sowing.url_video + '">video siembra</a> '
    from_email = os.getenv('FROM_EMAIL')
    email_to = user_donator.correo_electronico

    return send_email(from_email, email_to, subject, message)