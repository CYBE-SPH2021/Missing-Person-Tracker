from django.db import models

# Create your models here.

class acase(models.Model):

    case_id = models.AutoField(primary_key="True")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/case')
    address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    

    