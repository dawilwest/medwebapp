from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from users.forms import MyUserCreationForm, MedPractCreationForm, ProfileForm
from users.models import MyUser, SickUser, MedicalPractitioner
# Django Permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError


# Create your views here.


class SignUpView(CreateView):
    # This is a generic class that implements rendering forms and model creation
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    model = SickUser

    def form_valid(self, form):
        try:
            user = MyUser(
                username=form.cleaned_data["username"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            user.set_password(form.cleaned_data["password1"])
            user = form.save()
        except IntegrityError as e:
            return super().form_valid(form)
        else:
            form.instance.profile = user

        return super().form_valid(form)


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
    form_class = ProfileForm
    success_url = "/accounts/profile"
