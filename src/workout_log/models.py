from django.db import models


class Tag(models.Model):
    name = models.CharField()


class Exercise(models.Model):
    tags = models.ManyToManyField(
        Tag, through="ExerciseTagMap", related_name="exercises")
    name = models.CharField()

    notes = models.TextField(default="")


class ExerciseTagMap(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["tag", "exercise"],
                name="unique_exercise_tag"
            )
        ]


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, default=0, on_delete=models.CASCADE)
    weight = models.IntegerField()
    reps = models.IntegerField()

    date = models.DateTimeField(auto_now=True)
