from django.db import models

# Create your models here.


class Transaction(models.Model):
    title = models.CharField(max_length=20)
    amt = models.FloatField()
    date = models.DateTimeField()
    status = models.CharField(max_length=8, default='Pending')