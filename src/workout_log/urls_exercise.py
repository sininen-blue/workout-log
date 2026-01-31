from django.urls import path
from . import views_exercise

app_name = "exercise"

urlpatterns = [
    path("", views_exercise.index, name="index"),
    path("create", views_exercise.create, name="create"),
    path("store", views_exercise.store, name="store"),
    path("<int:exercise_id>/show", views_exercise.show, name="show"),
    path("<int:exercise_id>/edit", views_exercise.edit, name="edit"),
    path("<int:exercise_id>/update", views_exercise.update, name="update"),
    path("<int:exercise_id>/destroy", views_exercise.destroy, name="destroy"),

    # tags
    path("<int:exercise_id>/tag/create",
         views_exercise.create_tag, name="create_tag"),
    path("<int:exercise_id>/tag/<int:tag_id>/store",
         views_exercise.store_tag, name="store_tag"),
    path("<int:exercise_id>/tag/<int:tag_id>/destroy",
         views_exercise.destroy_tag, name="destroy_tag"),
]
