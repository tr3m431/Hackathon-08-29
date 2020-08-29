from django.db import models

# Create your models here.

# record each task
class Task(models.Model):
    # deadline
    deadline = models.DateField()

    # expected time to completion (in hours)
    time2complete = models.IntegerField()


# record the user's unavailable time
class UnavailableTime(models.Model):
    # time that the user is asleep or otherwise incapable/unwilling to be productive
    unavailableTimeStart = models.IntegerField()
    unavailableTimeEnd = models.IntegerField()
