from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
