from django.db import models
from cinemas.models import Cinema

class Film(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Ceance(models.Model):
    time = models.CharField(max_length=100)
    price = models.IntegerField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return self.time+" "+str(self.price)

class Place(models.Model):
    place = models.IntegerField()
    status = models.BooleanField(default=True)
    ceance = models.ForeignKey(Ceance, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.place)
