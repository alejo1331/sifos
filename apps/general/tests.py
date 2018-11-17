from django.test import TestCase

from .models import Municipio
from .models import Especie
from .models import EspecieMunicipio

# Create your tests here.
class MunicipioTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria Municipio")
        if (Municipio.objects.create(nombre='Villavicencio',longitd = "24.000", latitud="24.000")):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        municipio = Municipio.objects.get(id=1)
        print(municipio.nombre)
        print(municipio.longitd)
        print(municipio.latitud)
        
        
class EspecieTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria Especie")
        if (Especie.objects.create(nombre='Prueba',nombre_cientifico  = "prueba1", porcentaje_oxigeno="20%", porcentaje_carbono="15%")):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        especie = Especie.objects.get(id=1)
        if(especie):      
            print(especie.nombre)
            print(especie.nombre_cientifico)
            print(especie.porcentaje_oxigeno)
            print(especie.porcentaje_carbono)
        else:
            print("No Existe")
            
class RobotTests(TestCase):

    def setUp(self):
        print("Prueba Unitaria Robot")
        if (Robot.objects.create(nombre='Walle',gps  = "Prueba GPS", modelo="2016", estado="Bueno")):
            print("Exitoso")
        else:
            print("No Exitoso")

    def test_text_content(self):
        robot = Robot.objects.get(id=1)
        if(robot):      
            print(robot.nombre)
            print(robot.gps)
            print(robot.modelo)
            print(robot.estado)
        else:
            print("No Existe")

