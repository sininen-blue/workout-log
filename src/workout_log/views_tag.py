from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from typing import Optional

from .models import Tag, Set


def index(request: HttpRequest) -> HttpResponse:
    tags: QuerySet[Tag] = Tag.objects.all()

    context: dict[str, object] = {
        "tags": tags,
    }
    return render(request, "tag/index.html", context)


def create(request: HttpRequest) -> HttpResponse:
    return render(request, "tag/create.html")


def store(request: HttpRequest) -> HttpResponse:
    name: str = request.POST.get("name")

    try:
        Tag.objects.create(
            name=name,
        )
    except ValueError as v:
        messages.error(request, v)
    except Exception as e:
        messages.error(request, "Tag creation error: " + str(e))

    return redirect("tag:index")


def show(request: HttpRequest, tag_id: int) -> HttpResponse:
    tag: Tag = get_object_or_404(Tag, pk=tag_id)
    exercises = tag.exercises.all()
    sets_today = Set.objects.filter(
        date__date=datetime.today()
    ).all()

    grouped_exercises = []
    for exercise in exercises:
        grouped_exercises.append({
            "exercise": exercise,
            "tags": exercise.tags.all(),
            "done_count": range(_get_set_count(exercise, sets_today)),
        })

    context: dict[str, object] = {
        "tag": tag,
        "grouped_exercise": grouped_exercises
    }

    return render(request, "tag/show.html", context)


def edit(request: HttpRequest, tag_id: int) -> HttpResponse:
    tag: Tag = get_object_or_404(Tag, pk=tag_id)

    context: dict[str, object] = {
        "tag": tag
    }
    return render(request, "tag/edit.html", context)


def update(request: HttpRequest, tag_id: int) -> HttpResponse:
    name: Optional[str] = request.POST.get("name")

    tag: Tag = get_object_or_404(Tag, pk=tag_id)
    try:
        tag.name = name
        tag.save()
    except ValueError as v:
        messages.error(request, v)
    except Exception as e:
        messages.error(request, "Tag update error: " + str(e))

    return redirect("tag:index")


def destroy(request: HttpRequest, tag_id: int) -> HttpResponse:
    tag: Tag = get_object_or_404(Tag, pk=tag_id)
    try:
        tag.delete()
    except ValueError as v:
        messages.error(request, v)
    except Exception as e:
        messages.error(request, "Tag delete error: " + str(e))

    return redirect("tag:index")


def _get_set_count(exercise, sets):
    count = 0

    for exercise_set in sets:
        if exercise_set.exercise == exercise:
            count += 1

    return count
