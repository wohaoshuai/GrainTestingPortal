"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class User_mod(models.Model):
    user = models.OneToOneField(User)
    zipcode = models.FloatField(blank=False, default=00000)
    address = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)

class Reports(models.Model):
    user = models.ForeignKey(User)
    ptype = models.CharField(max_length=50, blank=False)
    min_price = models.FloatField(blank=False, default=00000)
    max_price = models.FloatField(blank=False, default=00000)
    date = models.DateField(blank=False)
    available = models.DateField(blank=False)
    quantity = models.FloatField(blank=False, default=00000)
    id1 = models.CharField(max_length=3, default=00000)
    temp = models.CharField(max_length=50, default=00000)
    humidity = models.CharField(max_length=50, default=00000)
