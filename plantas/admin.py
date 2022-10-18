from django.contrib import admin
from plantas.models import Planta

class Plantas(admin.ModelAdmin):
    list_display = ('id', 'plantName', 'airHumidity', 'soilMoisture', 'sunLight')
    list_display_links = ('id', 'plantName')
    search_fields = ('plantName',)


admin.site.register(Planta, Plantas)