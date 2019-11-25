from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from users.forms import MyUserCreationForm, MedPractCreationForm, ProfileForm, MedicalPractitionerProfileForm
from users.models import MyUser, SickUser, MedicalPractitioner
from data.models import BloodData, BodyMeasurementData, MedicalData, HospitalLocation
# Django Permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http.response import HttpResponseRedirect
from django.db import IntegrityError


# Create your views here.


class SignUpView(CreateView):
    # This is a generic class that implements rendering forms and model creation
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    model = MyUser

    def form_valid(self, form):
        super().form_valid(form)
        try:
            SickUser.objects.create(myuser=self.object)
        except IntegrityError:
            return super().form_valid(form)
        else:
            return HttpResponseRedirect(self.get_success_url())


class MedPractSignUpView(CreateView):
    # This is a generic class that implements rendering forms and model creation
    form_class = MedPractCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/practitioner/signup.html'
    model = MedicalPractitioner

    def form_valid(self, form):
        user = MyUser(
            username=form.cleaned_data["username"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
        )
        user.set_password(form.cleaned_data["password"])
        user.is_staff = True
        user.save()
        # Set permission for medical practitioner
        content_type = ContentType.objects.get_for_model(SickUser)
        permission = Permission.objects.get(
            codename='view_sickuser',
            content_type=content_type,
        )
        user.user_permissions.add(permission)
        user.save()
        # permission session ends here

        form.instance.title = form.cleaned_data["title"]
        form.instance.profile = user

        return super().form_valid(form)


class ProfileView(FormView):
    template_name = "users/user.html"
    # form_class = ProfileForm if not self.request.user else MedicalPractitionerProfileForm
    success_url = "/data/"

    def get_form_class(self):
        form_class = MedicalPractitionerProfileForm if self.request.user.is_staff else ProfileForm
        return form_class

    def get_context_data(self, **kwargs):
        contxt = super().get_context_data(**kwargs)
        user = self.request.user
        return contxt

    def form_valid(self, form):
        user = self.request.user
        if user.is_staff:
            data = form.cleaned_data
            print(data)
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.gender = data["gender"]
            user.date_of_birth = data["date_of_birth"]
            user.save()

            medicalpractitioner = MedicalPractitioner.objects.filter(myuser=user)[0]
            medicalpractitioner.phone = data["phone"]
            medicalpractitioner.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            data = form.cleaned_data
            print(data)
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.gender = data["gender"]
            # user.date_of_birth = data["date_of_birth"]
            user.save()

            sickuser = SickUser.objects.filter(myuser=user)[0]
            # sickuser.phone = data["phone"]
            sickuser.disease = data["medical_test"]
            sickuser.test_result = data["test_result"]
            sickuser.district = data["district"]
            sickuser.height = data["height"]
            sickuser.weight = data["weight"]
            sickuser.genotype = data["genotype"]
            sickuser.blood_group = data["blood_group"]
            sickuser.save()
            return HttpResponseRedirect(self.get_success_url())
