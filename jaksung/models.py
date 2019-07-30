from django.db import models

class Dong(models.Model):
    objects = models.Manager()
    message = models.TextField()
    writer = models.CharField(max_length=10)
    date = models.DateTimeField()


class Bang(models.Model):
    objects = models.Manager()
    message = models.TextField()
    writer = models.CharField(max_length=10)
    date = models.DateTimeField()
