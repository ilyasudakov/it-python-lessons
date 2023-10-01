from django.urls import path
from . import views

urlpatterns = [
    path("", views.patients, name="patients"),
    path("graphs", views.patients_graphs, name="patients_graphs"),
    path("<int:id>", views.patient_details, name="patient_details"),
]
