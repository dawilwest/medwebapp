from django.urls import path, include
from rest_framework import routers
from api.views import MedicalDataViewSet


router = routers.DefaultRouter()
router.register("data", MedicalDataViewSet)

urlpatterns = [
    path("", include(router.urls))
]
