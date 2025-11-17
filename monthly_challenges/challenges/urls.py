from django.urls import include, path
from . import views

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]

