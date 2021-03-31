from django.db import models

# Create your models here.

class acase(models.Model):
    MY_CHOICES = (
        ('Accepted', 'Accepted'),
        ('Ongoing', 'Ongoing'),
        
    )

    case_id = models.AutoField(primary_key="True")
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/case')
    info = models.CharField(max_length=200)
    status = models.CharField(max_length=100, choices=MY_CHOICES)
    

    