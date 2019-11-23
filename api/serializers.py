from rest_framework import serializers
from data.models import MedicalData, BloodData, HospitalLocation
from users.models import SickUser, MedicalPractitioner
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", 'email', 'first_name', 'last_name']


class SickUserSerializer(serializers.ModelSerializer):
    profile = UserSerializer()

    class Meta:
        model = SickUser
        fields = "__all__"


class MedicalPractitionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPractitioner
        fields = "__all__"


class MedicalDataSerializer(serializers.HyperlinkedModelSerializer):
    sickuser = SickUserSerializer()

    class Meta:
        model = MedicalData
        fields = ['illness', 'test_result', 'patient']
