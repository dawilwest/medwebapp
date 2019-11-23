from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class MyUser(AbstractUser):
    """
    fields: [
        first_name,
        last_name,
        middle_name(optional),
        gender,
        date_of_birth,
        marital_status,
        username,
        email,
        password,
    ]
    """
    # Limits the choice for Gender Selection
    SELECT_GENDER_OPTION = [('F', 'Female'), ('M', 'Male')]

    # Limits the choice for Marital Status Selection
    SELECT_MARITAL_STATUS = [('S', 'Single'), ('M', 'Married'), ('D', 'Divorced')]

    middle_name = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=SELECT_GENDER_OPTION)
    date_of_birth = models.DateField(blank=True, null=True)
    marital_status = models.CharField(max_length=10, choices=SELECT_MARITAL_STATUS)

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}"

    class Meta:
        verbose_name_plural = "Accounts"


class SickUser(models.Model):
    myuser = models.OneToOneField(
        # settings.AUTH_USER_MODEL,
        "users.MyUser",
        verbose_name="user name",
        on_delete=models.CASCADE,
        related_name="sickuser_user",
        blank=True,
        null=True
    )
    phone = models.CharField(verbose_name="phone number", max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.myuser}"

    def email(self):
        return self.myuser.email

    def birth_day(self):
        return self.myuser.date_of_birth

    def gender(self):
        return self.myuser.gender

    def marital_status(self):
        return self.myuser.marital_status


class MedicalPractitioner(models.Model):
    myuser = models.OneToOneField(
        # settings.AUTH_USER_MODEL,
        "users.MyUser",
        verbose_name="user name",
        on_delete=models.CASCADE,
        related_name="medicalpractitioner_user",
        blank=True,
        null=True
    )
    title = models.CharField(verbose_name="Title", max_length=50, blank=True, null=True)
    phone = models.CharField(verbose_name="phone number", max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.myuser}"

    def email(self):
        return self.myuser.email

    def username(self):
        return self.myuser.username
