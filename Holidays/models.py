from datetime import datetime

from django.db import models

# Create your models here.

class holidays(models.Model):
    holidays_name = models.TextField(default="Ничего")
    holidays_description = models.TextField(default="Cегодня праздников нет!")
    holidays_days = models.DateField(default=datetime.today)

    def __unicode__(self):
        return self.holidays_name

    def __str__(self):
        return self.holidays_name