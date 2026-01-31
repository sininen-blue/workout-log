from django.urls import path
from . import views

app_name = "set"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/exercise/<int:exercise_id>", views.create, name="create"),
    path("store", views.store, name="store"),
    path("<int:set_id>/show", views.show, name="show"),
    path("<int:set_id>/edit", views.edit, name="edit"),
    path("<int:set_id>/update", views.update, name="update"),
    path("<int:set_id>/destroy", views.destroy, name="destroy"),
]
