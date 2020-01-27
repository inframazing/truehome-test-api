from django.db import models


class Propiedad(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    square_meters = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=50)
