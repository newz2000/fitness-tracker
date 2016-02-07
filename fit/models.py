from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ExerciseTypes(models.Model):
    exercise = models.CharField(max_length=200)
    singular = models.CharField(max_length=200)
    
    def __str__(self):
        return self.exercise

class Workout(models.Model):
    user = models.ForeignKey(User)
    exercise = models.ForeignKey(ExerciseTypes)
    ts = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(default=1,
        help_text="In minutes")
    distance = models.DecimalField(max_digits=5, decimal_places=2, 
        null=True, blank=True, default=1.00, help_text="In miles")
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "%s on %s" % (self.exercise.exercise, self.ts.strftime('%a, %b %d %Y'))
        
