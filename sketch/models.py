from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
    class Meta:
        db_table = "Note"
    notes_title = models.CharField(max_length = 50)
    notes_description = models.TextField()
    notes_date = models.CharField(max_length = 11)
    notes_priority = models.IntegerField()

    def __str__(self):
        return self.notes_title