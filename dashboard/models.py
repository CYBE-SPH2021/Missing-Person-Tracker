from django.db import models

# Create your models here.

def case_directory_path(instance, filename): 
    name, ext = filename.split(".")
    name = "{}_{}_{}".format(instance.phoneno,instance.firstname,instance.lastname)
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
    emailid = models.CharField(max_length=200)

class camera(models.Model):
    ip_address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)


def missed_directory_path(instance, filename): 
    name, ext = filename.split(".")
    name = "{}_{}_{}".format(instance.firstname,instance.lastname,instance.landmark,instance.locality,instance.city)
    filename = name +'.'+ ext 
    return 'images/detected_missing/{}'.format(filename)
    
class detect_missing(models.Model):

    detectedcase_no = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to=missed_directory_path)
    landmark = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)

class detected_missing(models.Model):

    detectedcase_no = models.AutoField(primary_key = True)
    caseidentifier = models.CharField(max_length = 300)
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 200)
    phoneno = models.CharField(max_length = 200)
    image = models.ImageField(upload_to=missed_directory_path,unique = True)
    landmark = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    time_detected = models.CharField(max_length = 100)

class track_vehicle(models.Model):

    case = models.AutoField(primary_key = True)
    vehicle_no = models.CharField(max_length = 300)
