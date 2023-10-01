from django.shortcuts import render
from .models import Patient
from django.db import models


def patients(request):
    data = Patient.objects.all()
    return render(request, "table_view.html", {"data": data})


def patients_graphs(request):
    data = Patient.objects.all()
    return render(request, "graph_view.html", {"data": data})


def patient_details(request, id):
    data = Patient.objects.get(id=id)
    return render(request, "detail_view.html", {"data": data})
