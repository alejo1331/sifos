from rest_framework import routers, serializers, viewsets
from apps.general.views import  EspecieViewGet

router = routers.DefaultRouter()
router.register(r'especie/', EspecieViewGet)