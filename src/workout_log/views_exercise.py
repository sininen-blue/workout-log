from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db import IntegrityError
from django.db.models import QuerySet
from typing import Optional

from .models import Exercise, Tag, ExerciseTagMap


def index(request: HttpRequest) -> HttpResponse:
    exercises: QuerySet[Exercise] = Exercise.objects.prefetch_related(
        "tags").all()

    context: dict[str, object] = {
        "exercises": exercises,
    }
    return render(request, "exercise/index.html", context)


def create(request: HttpRequest) -> HttpResponse:
    return render(request, "exercise/create.html")


def store(request: HttpRequest) -> HttpResponse:
    name: str = request.POST.get("name")
    notes: Optional[str] = request.POST.get("notes")

    try:
        Exercise.objects.create(
            name=name,
            notes=notes
        )
    except Exception as e:
        messages.error(request, "exercise creation error: " + str(e))
        return redirect("exercise:index")

    return redirect("exercise:index")


def show(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise: Exercise = get_object_or_404(Exercise, pk=exercise_id)

    context: dict[str, object] = {
        "exercise": exercise
    }

    return render(request, "exercise/show.html", context)


def edit(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise: Exercise = get_object_or_404(Exercise, pk=exercise_id)

    context: dict[str, object] = {
        "exercise": exercise
    }
    return render(request, "exercise/edit.html", context)


def update(request: HttpRequest, exercise_id: int) -> HttpResponse:
    name: Optional[str] = request.POST.get("name")
    notes: Optional[str] = request.POST.get("notes")

    exercise: Exercise = get_object_or_404(Exercise, pk=exercise_id)
    exercise.name = name
    exercise.notes = notes
    exercise.save()

    return redirect("exercise:index")


def destroy(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise: Exercise = get_object_or_404(Exercise, pk=exercise_id)
    exercise.delete()

    return redirect("exercise:index")


def create_tag(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise: Exercise = get_object_or_404(Exercise, pk=exercise_id)
    tags: Tag = Tag.objects.all()

    context: dict[str, object] = {
        "exercise": exercise,
        "tags": tags
    }

    return render(request, "exercise/create_tag.html", context)


def store_tag(request: HttpRequest, exercise_id: int, tag_id: int) -> HttpResponse:
    exercise: Exercise = get_object_or_404(Exercise, pk=exercise_id)
    tag: Tag = get_object_or_404(Tag, pk=tag_id)

    try:
        ExerciseTagMap.objects.create(
            exercise=exercise,
            tag=tag,
        )
    except IntegrityError:
        messages.error(request, exercise.name +
                       " already has the tag: " + tag.name)
        return redirect("exercise:index")

    return redirect("exercise:index")


def destroy_tag(request: HttpRequest, exercise_id: int, tag_id: int) -> HttpResponse:
    exerciseTagMap: ExerciseTagMap = get_object_or_404(
        ExerciseTagMap, exercise=exercise_id, tag=tag_id)
    exerciseTagMap.delete()

    return redirect("exercise:index")
