from django.contrib import admin
from django.urls import path, include
from plantas.views import PlantasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'plants', PlantasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
