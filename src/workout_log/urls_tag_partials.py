from django.urls import path
from . import views_tag_partials

app_name = "tag_partials"

urlpatterns = [
    path("list", views_tag_partials.list, name="list"),
    path("attach_tag/<int:exercise_id>", views_tag_partials.attach_tag, name="attach_tag"),
    path("card/<int:tag_id>", views_tag_partials.card, name="card"),
]
