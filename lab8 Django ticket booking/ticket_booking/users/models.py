from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    priority = models.CharField(max_length=20, default='user')

    def __str__(self):
        data = {
            'email': self.email,
            'password': self.password,
            'fname': self.fname,
            'lname': self.lname,
            'priority': self.priority
        }
        return str(data)