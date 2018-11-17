from django.test import TestCase

from .models import Municipio

# Create your tests here.
class MunicipioTests(TestCase):

    def setUp(self):
        Municipio.objects.create(nombre='Villavicencio',longitd = "24.000", latitud="24.000")

    def test_text_content(self):
        municipio = Municipio.objects.get(id=1)
        expected_object_name = f'{Municipio.text}'
        self.assertEquals(expected_object_name, 'Villavicencio')

