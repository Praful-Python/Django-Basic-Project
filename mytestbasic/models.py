from django.db import models
from datetime import date

# Create your models here.
class Product(models.Model):
    red_date = models.DateField(default=date.today())
    customer_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=50)
    health_care = models.CharField(max_length=50, default="")
    Fee = models.IntegerField(default=0)
    desc = models.CharField(max_length=3000)


    def __str__(self):
        return self.patient_name

# Create your models here.
