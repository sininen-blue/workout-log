from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from typing import Optional

from .models import Tag


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
    except Exception as e:
        messages.error(request, "tag creation error: " + str(e))
        return redirect("tag:index")

    return redirect("tag:index")


def show(request: HttpRequest, tag_id: int) -> HttpResponse:
    tag: Tag = get_object_or_404(Tag, pk=tag_id)

    context: dict[str, object] = {
        "tag": tag
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
    notes: Optional[str] = request.POST.get("notes")

    tag: Tag = get_object_or_404(Tag, pk=tag_id)
    tag.name = name
    tag.save()

    return redirect("tag:index")


def destroy(request: HttpRequest, tag_id: int) -> HttpResponse:
    tag: Tag = get_object_or_404(Tag, pk=tag_id)
    tag.delete()

    return redirect("tag:index")
