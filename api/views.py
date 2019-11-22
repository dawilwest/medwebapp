# from django.shortcuts import render
from rest_framework import viewsets
from data.models import MedicalData
from api.serializers import MedicalDataSerializer

# Create your views here.


class MedicalDataViewSet(viewsets.ModelViewSet):
    queryset = MedicalData.objects.all()
    serializer_class = MedicalDataSerializer
