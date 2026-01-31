from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from typing import Optional

from .models import Tag


def index(request: HttpRequest) -> HttpResponse:
    exercises: QuerySet[Tag] = Tag.objects.all()

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
        Tag.objects.create(
            name=name,
            notes=notes
        )
    except Exception as e:
        messages.error(request, "exercise creation error: " + str(e))
        return redirect("exercise:index")

    return redirect("exercise:index")


def show(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise: Tag = get_object_or_404(Tag, pk=exercise_id)

    context: dict[str, object] = {
        "exercise": exercise
    }

    return render(request, "exercise/show.html", context)


def edit(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise: Tag = get_object_or_404(Tag, pk=exercise_id)

    context: dict[str, object] = {
        "exercise": exercise
    }
    return render(request, "exercise/edit.html", context)


def update(request: HttpRequest, exercise_id: int) -> HttpResponse:
    name: Optional[str] = request.POST.get("name")
    notes: Optional[str] = request.POST.get("notes")

    exercise: Tag = get_object_or_404(Tag, pk=exercise_id)
    exercise.name = name
    exercise.notes = notes
    exercise.save()

    return redirect("exercise:index")


def destroy(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise: Tag = get_object_or_404(Tag, pk=exercise_id)
    exercise.delete()

    return redirect("exercise:index")
