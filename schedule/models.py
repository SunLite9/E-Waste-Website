from django.db import models
from datetime import datetime

# Create your models here.
class BookAppointment(models.Model):
    name = models.CharField(max_length=40)
    phonenumber = models.CharField(max_length= 15)
    email = models.EmailField()
    address = models.CharField(max_length= 100)
    description = models.TextField()
    pickupdate = models.DateField(null=True)
    pickuptime = models.TimeField(null=True)
    image = models.ImageField(blank=True, upload_to="images/")
    booked_date = models.DateTimeField(default=datetime.now(), null=True)
    #Needs custom logic
    #scheduled_date =

    def __str__(self):
        return f'{self.name}-{self.phonenumber}'

