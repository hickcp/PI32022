from unittest.util import _MAX_LENGTH
from django.db import models

class Planta(models.Model):
    plantName = models.CharField(max_length=50)
    airHumidity = models.CharField(max_length=10)
    soilMoisture = models.CharField(max_length=10)
    sunLight = models.CharField(max_length=10)

    def __str__(self):
        return self.plantName
