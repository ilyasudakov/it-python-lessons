from django.db import models

# Create your models here.
class Patient(models.Model):
# id, age,   gender, height, weight,  ap_hi,  ap_lo, cholesterol,  gluc, smoke,  alco, active, cardio
# 0,  18393, 2,      168,    62.0,    110,    80,    1,            1,    0,      0,    1,      0
    age = models.IntegerField(max_length=100000)
    gender = models.CharField(choices=[(1, 'Male'), (2, 'Female')])
    height = models.IntegerField(max_length=300)
    weight = models.FloatField(max_length=400)
    ap_hi = models.IntegerField(max_length=300)
    ap_lo = models.IntegerField(max_length=300)
    cholesterol = models.BooleanField()
    gluc = models.BooleanField()
    smoke = models.BooleanField()
    alco = models.BooleanField()
    active = models.BooleanField()
    cardio = models.BooleanField()