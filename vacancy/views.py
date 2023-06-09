from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from .serializers import *


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()

        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def get_queryset(self):
        queryset = Region.objects.all()

        state = self.request.query_params.get('state')
        city = self.request.query_params.get('city')
        if state:
            queryset = queryset.filter(state__icontains=state)
        if city:
            queryset = queryset.filter(city__icontains=city)
        return queryset


class VacancyViewSet(viewsets.ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    basename = 'vacancy'

    def get_queryset(self):
        queryset = Vacancy.objects.all()

        title = self.request.query_params.get('title')
        salary = self.request.query_params.get('salary')
        state = self.request.query_params.get('state')
        if state:
            queryset = queryset.filter(state=state)
        if salary:
            queryset = queryset.filter(salary__icontains=salary)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    @action(detail=True, methods=['get'])
    def count(self, request, pk=None):
        instance = self.get_object()
        instance.count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TopVacancyView(viewsets.ModelViewSet):
    queryset = TopVacancy.objects.all()
    serializer_class = TopVacancySerializer
