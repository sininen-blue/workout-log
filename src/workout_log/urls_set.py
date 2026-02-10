from django.urls import path
from . import views_set

app_name = "set"

urlpatterns = [
    path("", views_set.index, name="index"),
    path("create/exercise/<int:exercise_id>", views_set.create, name="create"),
    path("store", views_set.store, name="store"),
    path("<int:set_id>/show", views_set.show, name="show"),
    path("<int:set_id>/edit", views_set.edit, name="edit"),
    path("<int:set_id>/update", views_set.update, name="update"),
    path("<int:set_id>/destroy", views_set.destroy, name="destroy"),
]
