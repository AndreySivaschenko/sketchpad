from django.contrib import admin

# Register your models here.
from Holidays.models import holidays

admin.site.register(holidays)