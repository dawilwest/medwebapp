from django.urls import path
from django.views.generic import TemplateView as temp_view
from data.views import StatisticsView, MedicalDataView, DashBoardView

app_name = "data"
urlpatterns = [
    # path("", temp_view.as_view(template_name="records/dashboard.html"), name="dashboard"),
    path("", DashBoardView.as_view(), name="dashboard"),
    path("statistics/", StatisticsView.as_view(), name="statistics"),
    path("medical/", MedicalDataView.as_view(), name="medical-data"),
]
