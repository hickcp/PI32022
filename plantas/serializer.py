from rest_framework import serializers
from plantas.models import Planta

class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta
        fields = ['id','plantName', 'airHumidity', 'soilMoisture', 'sunLight']