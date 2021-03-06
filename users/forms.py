from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import MyUser, MedicalPractitioner, SickUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
# The Form created below will be customized for the custom user model created.

username_validator = UnicodeUsernameValidator()


class MyUserCreationForm(UserCreationForm):

    class Meta:
        # A sub-class that provides meta-data to the ModelForm class
        model = MyUser
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', ]


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']


class MedPractCreationForm(forms.ModelForm):
    field_order = ['title', 'first_name', 'last_name', 'username', 'password']

    username = forms.CharField(validators=[username_validator])
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = MedicalPractitioner
        fields = ['title', 'first_name', 'last_name', 'email', 'username', 'password']


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    # middle_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(validators=[username_validator, ],
                               widget=forms.TextInput(attrs={'readonly': 'readonly'}),
                               required=False
                               )
    email = forms.EmailField(validators=[EmailValidator])
    gender = forms.ChoiceField(
        choices=(
            ('F', 'Female'),
            ('M', 'Male')
        )
    )
    birth_day = forms.DateField()
    marital_status = forms.ChoiceField(
        choices=(
                ('S', 'Single'),
                ('M', 'Married'),
                ('D', 'Divorced'),
        )
    )
    blood_group = forms.ChoiceField(
        choices=(
            ("A+", "A Positive"),
            ("A-", "A Negative"),
            ("B+", "B Positive"),
            ("B-", "B Negative"),
            ("O+", "O Positive"),
            ("O-", "O Negative"),
            ("AB+", "AB Positive"),
            ("AB-", "AB Negative"),
        )
    )
    genotype = forms.ChoiceField(
        choices=(
            ("AA", "AA"),
            ("AS", "AS"),
            ("SS", "SS"),
            ("AC", "AC"),
        )
    )
    height = forms.DecimalField()
    weight = forms.DecimalField()
    district = forms.ChoiceField(
        choices=(
            ("Maitama", "Maitama"),
            ("Garki", "Garki"),
            ("Asokoro", "Asokoro"),
            ("Wuse", "Wuse"),
            ("Jabi", "Jabi"),
            ("Karu", "Karu"),
        )
    )
    medical_test = forms.ChoiceField(
        choices=(
            ("Asthma", "Asthma"),
            ("Sickle Cell Disease", "Sickle Cell Disease"),
            ("Hypertension", "Hypertension"),
            ("Allergies", "Allergies"),
            ("Lung Disease", "Lung Disease"),
            ("Others", "Others"),
        )
    )
    test_result = forms.ChoiceField(widget=forms.CheckboxInput, choices=((True, True), (False, False)))


class MedicalPractitionerProfileForm(forms.Form):
    title = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=100)
    # middle_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(validators=[username_validator, ],
                               widget=forms.TextInput(attrs={'readonly': 'readonly'}),
                               required=False,
                               )
    email = forms.EmailField(validators=[EmailValidator])
    gender = forms.ChoiceField(
        choices=(
            ('M', "Male",),
            ('F', "Female",),
        )
    )
    date_of_birth = forms.DateField()
