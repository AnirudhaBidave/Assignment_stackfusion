from django.db import models

# Create your models here.
class submit_info(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    email = models.CharField(max_length=255)
    mob = models.IntegerField(max_length=10)
