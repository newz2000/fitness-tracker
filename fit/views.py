from django.shortcuts import render
from django.views import generic
from .models import Workout

# Create your views here.
class WorkoutView(generic.ListView):
    template_name = "fit/workouts.html"
    model = Workout

class WorkoutDetailView(generic.DetailView):
    template_name = "fit/workout-details.html"
    model = Workout
