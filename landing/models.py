from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
# Create your models here.
from django.utils import timezone


class comment(models.Model):
    class Meta:
            db_table = "Comments"

    comment_name = models.TextField()
    comment_email = models.EmailField()
    comment_date = models.DateField(auto_now=False, auto_now_add=True,null=True)
    comment_recall = models.TextField()

    def __str__(self):
        return str(self.comment_recall)

    def __unicode__(self):
        return str(self.comment_recall)




