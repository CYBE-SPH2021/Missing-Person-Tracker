from django.db import models


def missed_directory_path(instance, filename): 
    return 'images/vehicle/{}'.format(filename)

# Create your models here.
class detected_missing_vehicle(models.Model):

    detected_no = models.AutoField(primary_key = True)
    vehicle_no = models.CharField(max_length = 200)
    image = models.ImageField(upload_to=missed_directory_path,unique = True,max_length = 500)
    landmark = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    time_detected = models.CharField(max_length = 200)