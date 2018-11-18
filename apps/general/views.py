from rest_framework import  viewsets
from apps.general.models import Especie
from apps.general.EspecieSerializer import EspecieSerializer

class EspecieViewGet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer
