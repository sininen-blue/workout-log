from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet

from .models import Exercise, Set


def index(request: HttpRequest) -> HttpResponse:
    exerciseId: int = int(request.GET.get('exercise', '0'))

    exercises: QuerySet[Exercise] = Exercise.objects.all()
    sets: QuerySet[Set] = Set.objects.filter(exercise_id=exerciseId).all()

    context: dict[str, object] = {
        "exercises": exercises,
        "sets": sets,
    }
    print(context)

    return render(request, "statistics/index.html", context)


def weight_chart(request: HttpRequest) -> HttpResponse:
    exerciseId: int = int(request.GET.get('exercise', '0'))
    sets: QuerySet[Set] = Set.objects.filter(exercise_id=exerciseId).all()

    context: dict[str, object] = {
        "sets": sets,
    }

    return render(request, "statistics/components/weight_chart.html", context)
