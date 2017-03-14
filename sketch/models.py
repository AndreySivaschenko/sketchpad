from datetime import datetime

from django.db import models
from django.conf import settings

# Create your models here.
class Note(models.Model):
    class Meta:
        db_table = "Note"
        ordering = ('notes_time', )

    note_user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    notes_title = models.CharField(max_length = 50)
    notes_description = models.TextField()
    notes_time = models.TimeField(default=datetime.now)
    notes_date = models.DateField(default=datetime.today)
    notes_priority = models.IntegerField(default=0)


    def __str__(self):
        return self.notes_title

