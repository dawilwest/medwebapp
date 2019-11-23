from django.urls import path, include
from rest_framework import routers
from api.views import MedicalDataViewSet, SickUserViewSet, MedicalPractitionerViewSet, UserViewSet

router = routers.DefaultRouter()
router.register("data/medics", MedicalDataViewSet)
router.register("data/user", SickUserViewSet)
router.register("data/medicalpractitioner", MedicalPractitionerViewSet)
router.register("data/users", UserViewSet)

urlpatterns = [
    path("", include(router.urls))
]
