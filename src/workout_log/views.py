from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet

from .models import Exercise, Tag, Set


def index(request: HttpRequest) -> HttpResponse:
    today: date = timezone.localdate()

    sets: QuerySet[Set] = Set.objects.filter(
        date__date=today).order_by("-date")

    tags: QuerySet[Tag] = Tag.objects.filter(
        highlighted=True).prefetch_related("exercises").all()

    context: dict[str, object] = {
        "tags": tags,
        "sets": sets,
    }

    if request.headers.get("HX-Request"):
        return render(request, "day/index.html#day_page", context)

    return render(request, "day/index.html", context)
