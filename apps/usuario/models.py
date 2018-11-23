from django.db import models


# Create your models here.
class Donador(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    correo_electronico = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        db_table = 'usuario_donador'

    def __str__(self):
        return "{0}".format(self.nombre)
