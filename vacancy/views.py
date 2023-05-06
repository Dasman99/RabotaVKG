from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from .serializers import *


class CategoryAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RegionAPI(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


# class VacancyViewSet(generics.ListAPIView):
#     queryset = Vacancy.objects.all()
#     serializer_class = VacancySerializer

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    @action(detail=True, methods=['get'])
    def count(self, request, pk=None):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
