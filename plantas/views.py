from rest_framework import viewsets
from plantas.models import Planta
from plantas.serializer import PlantaSerializer

class PlantasViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

