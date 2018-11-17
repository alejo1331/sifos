from django.db import models
from django.db.models import Model, CASCADE
from django.utils.timezone import now
from apps.usuario.models import Donador
from decimal import Decimal


# Create your models here.
class Donacion(models.Model):
    valor = models.DecimalField(max_digits=30, decimal_places=0, default=Decimal(0))
    fecha = models.DateTimeField(default=now, blank=True)
    donador = models.ForeignKey(Donador, blank=False, null=False, on_delete=CASCADE)

    class Meta:
        db_table = 'financiacion_donacion'

    def __str__(self):
        return "{0}".format(self.nombre)