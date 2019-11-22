from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
from users.forms import MyUserCreationForm, MyUserChangeForm
from users.models import MyUser, SickUser, MedicalPractitioner
from data.admin import BloodDataInline, BodyMeasurementInline, MedicalDataInline, HospitalLocatioInline

# Register your models here.


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm

    models = MyUser
    list_display = ['pk', 'username', 'email', 'first_name', 'last_name', 'date_of_birth', 'gender', 'marital_status']


@admin.register(SickUser)
class SickUserAdmin(admin.ModelAdmin):
    inlines = [
        BloodDataInline,
        BodyMeasurementInline,
        MedicalDataInline,
        HospitalLocatioInline
    ]
    list_display = ['id', 'myuser', 'email', 'birth_day', 'gender', 'phone', 'address', 'marital_status']


@admin.register(MedicalPractitioner)
class MedicalPractitionerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'myuser', 'email', 'username', 'phone', 'address']
