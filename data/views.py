# from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import get_user_model
from users.models import SickUser, MedicalPractitioner
from data.models import MedicalData
# Create your views here.


class DashBoardView(LoginRequiredMixin, TemplateView):
    User = get_user_model()
    users_count = User.objects.all().count()
    user_count = SickUser.objects.all().count()
    medicalpractitioner_count = MedicalPractitioner.objects.all().count()

    extra_context = {
        "users_count": users_count,
        "user_count": user_count,
        "medicalpractitioner_count": medicalpractitioner_count,
    }
    template_name = "data/dashboard.html"


class StatisticsView(LoginRequiredMixin, ListView):
    # All Users can View this page as long as they are logged into their accounts
    User = get_user_model()
    users_count = User.objects.all().count()
    user_count = SickUser.objects.all().count()
    medicalpractitioner_count = MedicalPractitioner.objects.all().count()
    medical_data_count = MedicalData.objects.all().count()

    medical_data = MedicalData.objects.all()

    queryset = SickUser.objects.all()
    context_object_name = "sickusers_list"
    template_name = "data/sickuser_statistics.html"
    try:
        extra_context = {
                "users_count": users_count,
                "user_count": round(user_count / users_count) * 100,
                "medicalpractitioner_count": round((medicalpractitioner_count / users_count) * 100, 1),
                "medical_data_count": medical_data_count,


                # Data Table
                "asthma": medical_data.filter(disease__startswith="Asthma").count,
                "asthma_percentage": round((medical_data.filter(disease__startswith="Asthma").count() / medical_data.count()) * 100),
                "sicklecelldisease": medical_data.filter(disease__startswith="Sickle Cell Disease").count(),
                "sicklecelldisease_percentage": round((medical_data.filter(disease__startswith="Sickle Cell Disease").count() / medical_data.count()) * 100),
                "hypertension": medical_data.filter(disease__startswith="Hypertension").count,
                "hypertensioin_percentage": round((medical_data.filter(disease__startswith="Hypertension").count() / medical_data.count()) * 100),
                "allergies": medical_data.filter(disease__startswith="Allergies").count,
                "allergies_percentage": round((medical_data.filter(disease__startswith="Allergies").count() / medical_data.count()) * 100),
                "lungdisease": medical_data.filter(disease__startswith="Lung Disease").count,
                "lungdisease_percentage": round((medical_data.filter(disease__startswith="Lung Disease").count() / medical_data.count()) * 100),
                "others": medical_data.filter(disease__startswith="Others").count,
                "others_percentage": round((medical_data.filter(disease__startswith="Others").count() / medical_data.count()) * 100),
        }
    except ZeroDivisionError:
        pass


class MedicalDataView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    # Only Users logged in as Medical Practitioners can view this page
    model = SickUser
    context_object_name = "sickuser_list"
    permission_required = ('users.view_sickuser')
    template_name = "data/sickuser_list.html"
