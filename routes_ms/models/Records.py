from djongo import models

class Record(models.Model):
    date = models.DateTimeField()
    startLatitude = models.FloatField()
    startLongitude = models.FloatField()
    endLatitude = models.FloatField()
    endLongitude = models.FloatField()
    startAddress = models.CharField(max_length=200)
    endAddress = models.CharField(max_length=200)
    userId = models.IntegerField()
