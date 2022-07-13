from django.db import models
from django.urls import reverse

TYPES = (
    ('W', 'Watering'), 
    ('F', 'Fertilization'), 
    ('R', 'Repotting')
)

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=50)
    difficultyLevel = models.IntegerField()
    waterFrequency = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id':self.id})

class Watering(models.Model):
    date = models.DateField()
    type = models.CharField(
        max_length=1,
        choices=TYPES, 
        default=TYPES[0][0]
    )

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']