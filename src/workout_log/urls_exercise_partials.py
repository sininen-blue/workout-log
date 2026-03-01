from django.urls import path
from . import views_exercise_partials

app_name = "exercise_partials"

urlpatterns = [
    path("list", views_exercise_partials.list, name="list"),
]
