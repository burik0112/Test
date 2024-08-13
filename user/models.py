from django.db import models


# Create your models here.


class TimeSheet(models.Model):
    Working = models.BooleanField()
    TimeSheetCodeEN = models.CharField(max_length=56)
    TimeSheetCodeRU = models.CharField(max_length=56)
    TimeSheetCodeTR = models.CharField(max_length=56)
    TimeSheetCode = models.CharField(max_length=10)
    DescriptionRU = models.TextField()

    def __str__(self):
        return self.TimeSheetCodeEN
