from django.db import models


class Exercise(models.Model):
    name = models.CharField()

    notes = models.TextField(default="")


class Tag(models.Model):
    name = models.CharField()


class ExerciseTagMap(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Set(models.Model):
    weight = models.IntegerField()
    reps = models.IntegerField()

    date = models.DateTimeField(auto_now=True)
