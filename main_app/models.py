from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=50)
    difficultyLevel = models.IntegerField()
    waterFrequency = models.CharField(max_length=100)

    def __str__(self):
        return self.name