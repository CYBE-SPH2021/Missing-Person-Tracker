from django.db import models

# Create your models here.

def case_directory_path(instance, filename): 
    name, ext = filename.split(".")
    name = "{}{}{}".format(instance.phoneno,instance.firstname,instance.lastname)
    filename = name +'.'+ ext 
    return 'images/case/{}'.format(filename)

class acase(models.Model):

    case_id = models.AutoField(primary_key="True")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    image = models.ImageField(upload_to=case_directory_path)
    address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=100)

    

    