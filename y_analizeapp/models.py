from django.db import models
from datetime import date
from django.utils.timezone import now

class test_database(models.Model):
    int_eria = models.IntegerField(default=0)
    str_eria = models.CharField(max_length=10)
    str_eria = models.CharField(max_length=10)
    def __str__(self):
        return self.name