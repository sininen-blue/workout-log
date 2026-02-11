from django.urls import path
from . import views_statistics

app_name = "statistics"

urlpatterns = [
    path("", views_statistics.index, name="index"),
    path("weight_chart", views_statistics.weight_chart, name="weight_chart"),
]
