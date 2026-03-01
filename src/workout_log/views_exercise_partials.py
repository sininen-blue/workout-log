from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db import IntegrityError
from django.db.models import QuerySet
from typing import Optional

from .models import Exercise, Tag, ExerciseTagMap


def list(request: HttpRequest) -> HttpResponse:
    exercises: QuerySet[Exercise] = Exercise.objects.prefetch_related(
        "tags").all()

    context: dict[str, object] = {
        "exercises": exercises,
    }

    response: HttpResponse = render(request, "exercise/index.html#exercise_list", context)

    return response
