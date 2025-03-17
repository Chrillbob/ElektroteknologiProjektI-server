from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Measurements(models.Model):
    temp = models.FloatField("temperature measurement")
    humidity = models.FloatField("humidity measurement")
    wind_speed = models.FloatField("wind speed")
    wind_dir = models.CharField("wind direction", max_length=2)
    pressure = models.FloatField("air pressure")
    smoke = models.IntegerField("smoke level")
    ambient = models.FloatField("ambient light level")
    meas_time = models.DateTimeField("measurement time")

    def __str__(self):
        return "Measurement at " + self.meas_time.isoformat()