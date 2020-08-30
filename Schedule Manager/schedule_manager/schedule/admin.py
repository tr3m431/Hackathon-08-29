from django.contrib import admin

# Register your models here.
from .models import Task, UnavailableTime

admin.site.register(Task)
admin.site.register(UnavailableTime)
