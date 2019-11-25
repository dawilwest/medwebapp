from django.db import models
from users.models import SickUser
# Create your models here.


class BloodData(models.Model):
    BLOOD_GROUP = (
        ("A+", "A Positive"),
        ("A-", "A Negative"),
        ("B+", "B Positive"),
        ("B-", "B Negative"),
        ("O+", "O Positive"),
        ("O-", "O Negative"),
        ("AB+", "AB Positive"),
        ("AB-", "AB Negative"),
    )

    GENOTYPE = (
        ("AA", "AA"),
        ("AS", "AS"),
        ("SS", "SS"),
        ("AC", "AC"),
    )

    myuser = models.OneToOneField(
        'users.SickUser',
        on_delete=models.CASCADE,
        related_name="sickuser_blooddata"
    )
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP)
    genotype = models.CharField(max_length=5, choices=GENOTYPE)

    def __str__(self):
        return f"{self.myuser} Blood Details(Blood Group and Genotype)"


class BodyMeasurementData(models.Model):
    myuser = models.OneToOneField(
        'users.SickUser',
        on_delete=models.CASCADE,
        related_name="sickuser_bodymeasurement"
    )

    height = models.DecimalField(verbose_name="Height (m)", max_digits=5, decimal_places=2)
    weight = models.DecimalField(verbose_name="Weight (Kg)", max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.myuser} Body Measurement (Height and Weight)"


class MedicalData(models.Model):
    TYPE_OF_SICKNESS = (
        ("Asthma", "Asthma"),
        ("Sickle Cell Disease", "Sickle Cell Disease"),
        ("Hypertension", "Hypertension"),
        ("Allergies", "Allergies"),
        ("Lung Disease", "Lung Disease"),
        ("Others", "Others"),
    )
    disease = models.CharField(max_length=200, choices=TYPE_OF_SICKNESS)
    sickuser = models.OneToOneField("users.SickUser", on_delete=models.CASCADE, related_name="sickuser_data")
    test_result = models.BooleanField(default=False)

    def __str__(self):
        return self.disease


class HospitalLocation(models.Model):
    DISTRICT = (
        ("Maitama", "Maitama"),
        ("Garki", "Garki"),
        ("Asokoro", "Asokoro"),
        ("Wuse", "Wuse"),
        ("Jabi", "Jabi"),
        ("Karu", "Karu"),
    )
    town = models.CharField(max_length=200, default="Abuja")
    district = models.CharField(max_length=200, choices=DISTRICT)
    sickuser = models.OneToOneField("users.SickUser", on_delete=models.CASCADE, related_name="sickuser_hospital_location")

    def __str__(self):
        return f"{self.district}, {self.town}"
