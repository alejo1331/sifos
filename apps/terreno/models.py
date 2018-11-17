from django.db import models
from apps.general.models import Municipio, TipoPatron, Especie, Robot
from apps.financiacion.models import Donacion
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Model, CASCADE


# Create your models here.
class Poligono(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    coordenadas_puntos = models.CharField(max_length=5000, blank=True, null=True)
    area = models.FloatField(max_length=100, blank=True, null=True)
    perimetro = models.FloatField(max_length=100, blank=True, null=True)
    tipo_patron = models.ForeignKey(TipoPatron, blank=False, null=False, on_delete=CASCADE)
    municipio = models.ForeignKey(Municipio, blank=False, null=False, on_delete=CASCADE)
    usuario = models.ForeignKey(User, blank=False, null=False, on_delete=CASCADE)


    class Meta:
        db_table = 'terreno_poligono'

    def __str__(self):
        return "{0}".format(self.nombre)

# Create your models here.
class PuntoSiembra(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    latitud = models.FloatField(max_length=200, blank=True, null=True)
    longitud = models.FloatField(max_length=200, blank=True, null=True)
    poligono = models.ForeignKey(Poligono, blank=False, null=False, on_delete=CASCADE)
    especie = models.ForeignKey(Especie, blank=False, null=False, on_delete=CASCADE)

    class Meta:
        db_table = 'terreno_punto_siembra'

    def __str__(self):
        return "{0}".format(self.nombre)

# Create your models here.
class Siembra(models.Model):
    temperatura = models.CharField(max_length=5, blank=True, null=True)
    humedad = models.CharField(max_length=5, blank=True, null=True)
    altitud = models.FloatField(max_length=200, blank=True, null=True)
    ph = models.CharField(max_length=5, blank=True, null=True)
    url_video = models.CharField(max_length=200, blank=True, null=True)
    punto_siembra = models.OneToOneField( PuntoSiembra, on_delete=models.CASCADE, primary_key=True )
    robot = models.ForeignKey(Robot, blank=True, null=True, on_delete=CASCADE)
    donacion = models.ForeignKey(Donacion, blank=False, null=False, on_delete=CASCADE)

    class Meta:
        db_table = 'terreno_siembra'

    def __str__(self):
        return "{0}".format(self.nombre)