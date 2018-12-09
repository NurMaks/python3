from django.db import models
from films.models import Place

class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    priority = models.CharField(max_length=20, default="user")

    def __str__(self):
        return self.fname+" "+self.lname
    
class MyTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
