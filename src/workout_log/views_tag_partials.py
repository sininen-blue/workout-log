from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse

from .models import Tag


def card(request: HttpRequest, tag_id: int) -> HttpResponse:
    tag: Tag = get_object_or_404(Tag, pk=tag_id)

    context: dict[str, object] = {
        "tag": tag
    }

    return render(request, "tag/index.html#tag_card", context)
