from djongo import models

class FavPlace(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    userId = models.IntegerField()