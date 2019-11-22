from django.urls import path
from users.views import SignUpView, MedPractSignUpView, ProfileView

app_name = "users"
urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('practitioner/signup/', MedPractSignUpView.as_view(), name='practitioner-signup'),
]
