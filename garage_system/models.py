from django.db import models
from django.urls import reverse
from django_unixdatetimefield import UnixDateTimeField

VEHICLE_TYPE = (
    ("LIGHT VEHICLE", "light vehicle"),
    ("HEAVY VEHICLE", "heavy vehicle"),
    ("TWO WHEELER", "two wheeler"),
)

# Create your models here.
class Spot(models.Model):
    spot_type = models.CharField(max_length=255)

    def __str__(self):
        self.spot_type

class Ticket(models.Model):

    name = models.CharField(max_length=256)
    entry_time = UnixDateTimeField()
    exit_time = UnixDateTimeField()
    ticket_price = models.IntegerField(max_length=9)
    paid = models.BooleanField()
    vehicle_registration_no = models.CharField(max_length=255)
    spot = models.ForeignKey(Spot, related_name='tickets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ParkingPrice(models.Model):
    type = models.CharField('Vehicle Type', max_length=150, choices=VEHICLE_TYPE , default="light vehicle")
    price = models.IntegerField(max_length=11)

    def __str__(self):
        self.type


