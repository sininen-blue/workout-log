from django.urls import path
from . import views_tag

app_name = "tag"

urlpatterns = [
    path("", views_tag.index, name="index"),
    path("create", views_tag.create, name="create"),
    path("store", views_tag.store, name="store"),
    path("<int:tag_id>/show", views_tag.show, name="show"),
    path("<int:tag_id>/edit", views_tag.edit, name="edit"),
    path("<int:tag_id>/update", views_tag.update, name="update"),
    path("<int:tag_id>/destroy", views_tag.destroy, name="destroy"),
]
