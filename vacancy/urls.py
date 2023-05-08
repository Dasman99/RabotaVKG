from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'category', CategoryView)
router.register(r'region', RegionView)
router.register(r'vacancy', VacancyViewSet)
router.register(r'company', CompanyView)
router.register(r'topvacancy', TopVacancyView)

urlpatterns = [
    path('', include(router.urls)),
]