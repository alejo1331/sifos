from django.test import TestCase
'''
from .models import Poligono
from .models import PuntoSiembra
from .models import Siembra
from apps.general.models import Municipio, TipoPatron, Especie, Robot
from apps.financiacion.models import Donacion
from django.contrib.auth.models import User

# Create your tests here.
class PoligonoTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria Poligono")
        if (Poligono.objects.create(nombre='Villavicencio',coordenadas_puntos = "24.000", tipo_patron = TipoPatron.object.get(pk=1), municipio =  Municipio.object.get(pk=1), usuario =  User.object.get(pk=1))):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        poligono = Poligono.objects.get(id=1)
        print(poligono.nombre)
        print(poligono.coordenadas_puntos)
     
# Create your tests here.
class PuntoSiembraTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria PuntoSiembra")
        if (PuntoSiembra.objects.create(nombre='Villavicencio',latitud = "24.000",longitud = "24.000", poligono = 1, especie = 1)):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        puntoSiembra = PuntoSiembra.objects.get(id=1)
        print(puntoSiembra.nombre)
        print(puntoSiembra.longitd)
        print(puntoSiembra.latitud)
        
# Create your tests here.
class SiembraTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria Siembra")
        if (Siembra.objects.create(temperatura='Villavicencio',altitud = "24.000",humedad = "24.000", punto_siembra = 1, donacion = 1)):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        siembra = Siembra.objects.get(id=1)
        print(siembra.temperatura)
        print(siembra.humedad)
        print(siembra.altitud)
        '''
