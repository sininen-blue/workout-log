from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet

from .models import Tag


def list(request: HttpRequest) -> HttpResponse:
    tags: QuerySet[Tag] = Tag.objects.all()

    context: dict[str, object] = {
        "tags": tags,
    }

    response: HttpResponse = render(request, "tag/partials.html#tag_list", context)
    return response


def attach_tag(request: HttpRequest, exercise_id: int) -> HttpResponse:
    tags: QuerySet[Tag] = Tag.objects.all()

    context: dict[str, object] = {
        "tags": tags,
        "exercise_id": exercise_id,
    }

    response: HttpResponse = render(request, "tag/partials.html#attach_tag", context)
    return response


def card(request: HttpRequest, tag_id: int) -> HttpResponse:
    tag: Tag = get_object_or_404(Tag, pk=tag_id)

    context: dict[str, object] = {
        "tag": tag
    }

    return render(request, "tag/index.html#tag_card", context)
