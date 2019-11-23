# from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from data.models import MedicalData
from users.models import SickUser, MedicalPractitioner
from api.serializers import MedicalDataSerializer, UserSerializer, SickUserSerializer, MedicalPractitionerSerializer
# Create your views here.


class MedicalDataViewSet(viewsets.ModelViewSet):
    queryset = MedicalData.objects.all()
    serializer_class = MedicalDataSerializer


class SickUserViewSet(viewsets.ModelViewSet):
    queryset = SickUser.objects.all()
    serializer_class = SickUserSerializer


class MedicalPractitionerViewSet(viewsets.ModelViewSet):
    queryset = MedicalPractitioner.objects.all()
    serializer_class = MedicalPractitionerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
