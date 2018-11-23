from rest_framework import serializers
from apps.general.models import Especie

class EspecieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Especie
        fields = ('nombre', 'nombre_cientifico')
