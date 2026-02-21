from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    name = models.CharField(default="")

    highlighted = models.BooleanField(default=True)


class Exercise(models.Model):
    tags = models.ManyToManyField(
        Tag, through="ExerciseTagMap", related_name="exercises")
    name = models.CharField()
    notes = models.TextField(default="")

    active = models.BooleanField(default=False)


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


class Session(models.Model):
    notes = models.TextField(default="")
    rating = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    date = models.DateTimeField(auto_now_add=True)


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, null=True, on_delete=models.CASCADE)

    weight = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)

    notes = models.TextField(default="")
    rating = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    date = models.DateTimeField(auto_now_add=True)
