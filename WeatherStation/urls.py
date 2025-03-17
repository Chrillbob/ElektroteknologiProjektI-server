from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:meas_id>/", views.measurement, name="measurement"),
    path("latest/", views.latest, name="latest"),
    path("lastday/", views.lastday, name="lastday")
]