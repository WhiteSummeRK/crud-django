from datetime import datetime
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)

    def __repr__(self):
        return "Nome: {} | Email: {}".format(self.name, self.mail)


class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=500)
    date = models.DateField(auto_now=True)

    def publish(self):
        self.date = timezone.now()
        self.save()
