from django.urls import path
from . import views_tag_partials

app_name = "tag_partials"

urlpatterns = [
    path("card/<int:tag_id>", views_tag_partials.card, name="card"),
]
