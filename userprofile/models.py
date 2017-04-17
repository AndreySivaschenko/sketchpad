from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

    user = models.OneToOneField(User)
    avatar = models.ImageField(verbose_name='Изображение')
    dateBirth = models.DateField(default=datetime.today)
    phone = models.CharField(max_length=12,blank=True)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

User.profile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])