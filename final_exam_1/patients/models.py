from django.db import models


# Create your models here.
class Patient(models.Model):
    age = models.IntegerField(help_text="Age in days")
    gender = models.CharField(
        choices=[(1, "Male"), (2, "Female"), (3, "Nonbinary")], max_length=1
    )
    height = models.IntegerField(help_text="centimeters")
    weight = models.FloatField()
    ap_hi = models.IntegerField()
    ap_lo = models.IntegerField()
    cholesterol = models.IntegerField()
    gluc = models.IntegerField()
    smoke = models.BooleanField()
    alco = models.BooleanField()
    active = models.BooleanField()
    cardio = models.BooleanField()

    @property
    def bmi(self):
        _height = self.height / 100
        return int(self.weight / (_height * _height))
