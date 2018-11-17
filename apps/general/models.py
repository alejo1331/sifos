from django.db import models
from django.db.models import Model, CASCADE

ESTADOS = {
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo')
}


# Create your models here.
class Municipio(models.Model):
    nombre = models.CharField(max_length=150, blank=True, null=True)
    longitd = models.CharField(max_length=150, blank=True, null=True)
    latitud = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'general_municipio'

    def __str__(self):
        return "{0}".format(self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(Municipio, self).save(*args, **kwargs)


# Create your models here.
class Especie(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    nombre_cientifico = models.CharField(max_length=200, blank=True, null=True)
    porcentaje_oxigeno = models.CharField(max_length=100, blank=True, null=True)
    porcentaje_carbono = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'general_especie'

    def __str__(self):
        return "{0}".format(self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(Especie, self).save(*args, **kwargs)


# Create your models here.
class EspecieMunicipio(models.Model):
    especie = models.ForeignKey(Especie, blank=False, null=False, on_delete=CASCADE)
    municipio = models.ForeignKey(Municipio, blank=False, null=False, on_delete=CASCADE)

    class Meta:
        db_table = 'general_especie_municipio'

    def __str__(self):
        return "{0}".format(self.municipio.nombre + " - " + self.especie.nombre)


# Create your models here.
class TipoPatron(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    figura = models.CharField(max_length=200, blank=True, null=True)
    distancia_interna = models.IntegerField(blank=False, null=True, default=1)

    class Meta:
        db_table = 'general_tipo_patron'

    def __str__(self):
        return "{0}".format(self.nombre)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(Municipio, self).save(*args, **kwargs)


class Robot(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    gps = models.CharField(max_length=200, blank=True, null=True)
    modelo = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='Activo', blank=False, null=False)

    class Meta:
        db_table = 'general_robot'

    def __str__(self):
        return "{0}".format(self.nombre)
