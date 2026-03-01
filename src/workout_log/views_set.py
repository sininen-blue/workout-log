from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet

from .models import Exercise, Set, Session


def index(request: HttpRequest) -> HttpResponse:
    sets: QuerySet[Set] = Set.objects.order_by("-date").all()

    context: dict[str, object] = {
        "sets": sets,
    }
    return render(request, "set/index.html", context)


def create(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise: Exercise = get_object_or_404(Exercise, pk=exercise_id)

    latestSet: Set = Set.objects.order_by("-date")
    latestSet = latestSet.filter(exercise=exercise)
    latestSet = latestSet.first()

    context: dict[str, object] = {
        "exercise": exercise,
        "latestSet": latestSet
    }
    return render(request, "set/create.html", context)


def store(request: HttpRequest) -> HttpResponse:
    exercise_id: int = int(request.POST.get("id"))
    weight: int = int(request.POST.get("weight"))
    reps: int = int(request.POST.get("reps"))

    exercise: Exercise = get_object_or_404(Exercise, pk=exercise_id)

    current_datetime: datetime = timezone.now()
    threshold_datetime: datetime = current_datetime - timedelta(hours=3.0)

    session: Session = Session.objects.filter(
        date__gte=threshold_datetime
    ).exists()

    print(session, "\n\n\n")

    if not session:
        try:
            session = Session.objects.create(
                notes="",
            )
        except Exception as e:
            messages.error(request, "Session creation error: " + str(e))
    else:
        session = Session.objects.filter(
            date__gte=threshold_datetime
        ).first()

    try:
        Set.objects.create(
            exercise=exercise,
            session=session,

            weight=weight,
            reps=reps,

            notes="",
            rating=3,
        )
    except ValueError as v:
        messages.error(request, v)
    except Exception as e:
        messages.error(request, "Set creation error: " + str(e))

    return redirect("day:index")


def show(request: HttpRequest, exercise_id: int) -> HttpResponse:
    exercise: Exercise = get_object_or_404(Exercise, pk=exercise_id)

    context: dict[str, object] = {
        "exercise": exercise
    }

    return render(request, "exercise/show.html", context)


def edit(request: HttpRequest, set_id: int) -> HttpResponse:
    exerciseSet: Set = get_object_or_404(Set, pk=set_id)

    context: dict[str, object] = {
        "set": exerciseSet
    }
    return render(request, "day/edit.html", context)


def update(request: HttpRequest, set_id: int) -> HttpResponse:
    weight: int = int(request.POST.get("weight"))
    reps: int = int(request.POST.get("reps"))

    exerciseSet: Set = get_object_or_404(Set, pk=set_id)
    try:
        exerciseSet.weight = weight
        exerciseSet.reps = reps
        exerciseSet.save()
    except ValueError as v:
        messages.error(request, v)
    except Exception as e:
        messages.error(request, "Set update error: " + str(e))

    return redirect("day:index")


def destroy(request: HttpRequest, set_id: int) -> HttpResponse:
    exerciseSet: Set = get_object_or_404(Set, pk=set_id)
    try:
        exerciseSet.delete()
    except ValueError as v:
        messages.error(request, v)
    except Exception as e:
        messages.error(request, "Set delete error: " + str(e))

    return redirect("day:index")
