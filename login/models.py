from django.db import models

# Create your models here.

class Suspect(models.Model):
    ids = models.AutoField(primary_key="True")
    landmark = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    
    

    