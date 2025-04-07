from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Measurements(models.Model):
    temp = models.FloatField("temperature measurement")
    humidity = models.FloatField("humidity measurement")
    wind_speed = models.FloatField("wind speed")
    wind_dir = models.FloatField("wind direction")
    pressure = models.FloatField("air pressure")
    smoke = models.FloatField("smoke level")
    ambient = models.FloatField("ambient light level")
    meas_time = models.DateTimeField("measurement time", default=timezone.localtime(timezone=timezone.get_default_timezone()))

    def __str__(self):
        return "Measurement at " + self.meas_time.isoformat()