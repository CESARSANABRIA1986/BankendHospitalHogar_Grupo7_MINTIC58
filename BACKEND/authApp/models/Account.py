from django.db import models
from .User import User

class Account(models.Model):
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    lastChangeDate = models.DateTimeField()
    isActive = models.BooleanField(default=True)