from django.db import models


class Route(models.Model):
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    stops = models.TextField()
    travel_time = models.TextField()
