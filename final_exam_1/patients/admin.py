from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientModel(admin.ModelAdmin):
    list_display = ["id", "age"]

    readonly_fields = ["id"]
    fields = [
        "age",
        "gender",
        "height",
        "weight",
        "ap_hi",
        "ap_lo",
        "cholesterol",
        "gluc",
        "smoke",
        "alco",
        "active",
        "cardio",
    ]
