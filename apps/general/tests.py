from django.test import TestCase

from .models import Municipio

# Create your tests here.
class MunicipioTests(TestCase):

    def setUp(self):
        if (Municipio.objects.create(nombre='Villavicencio',longitd = "24.000", latitud="24.000")):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        municipio = Municipio.objects.get(id=1)
        print(municipio.nombre)
        print(municipio.longitd)
        print(municipio.latitud)

