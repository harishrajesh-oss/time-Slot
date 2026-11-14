from django.db import models

# Create your models here.
class TimeSlot(models.Model):
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50, blank=True)  # additional task 1

    def _str_(self):
        return f"{self.day} {self.start_time}-{self.end_time}"
