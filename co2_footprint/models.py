from django.db import models

class CO2_footprint(models.Model):
    name = models.CharField(max_length=50)
    electricity = models.FloatField(null=True)
    travel = models.FloatField(null=True)
    electronics_devices = models.FloatField(null=True)
    food_habbit = models.CharField(max_length=50)
    water = models.FloatField(null=True)
    waste = models.FloatField(null=True)
    daily_co2_emission = models.FloatField()
    yearly_co2_emission = models.FloatField()

    class Meta:
        db_table = "co2_footprint"

