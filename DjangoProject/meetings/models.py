from django.db import models
from datetime import time

# Create your models here.

class Room(models.Model):

    R_name = models.CharField(max_length=200)
    Floor_number = models.IntegerField()
    R_number = models.IntegerField()

    def __str__(self):
        return f"{self.R_name} on {self.Floor_number} with Room number{self.R_number}"
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date=models.DateField()
    start_time=models.TimeField(default = time(9))
    duration=models.IntegerField(default = 1)
    room=models.ForeignKey(Room,on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"


