from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'category', CategoryAPI)
router.register(r'region', RegionAPI)
router.register(r'vacancy', VacancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]