from django.contrib import admin
from .models import ExerciseTypes, Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise', 'ts')
    list_filter = ['exercise', 'user', 'ts']

# Register your models here.
admin.site.register(ExerciseTypes)
admin.site.register(Workout, WorkoutAdmin)