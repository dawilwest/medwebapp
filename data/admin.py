from django.contrib import admin
from data.models import BloodData, BodyMeasurementData, MedicalData, HospitalLocation

# Register your models here.


class BloodDataInline(admin.TabularInline):
    model = BloodData


class BodyMeasurementInline(admin.TabularInline):
    model = BodyMeasurementData


class MedicalDataInline(admin.TabularInline):
    model = MedicalData


class HospitalLocatioInline(admin.TabularInline):
    model = HospitalLocation
