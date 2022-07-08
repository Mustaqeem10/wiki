from django.urls import path

from . import views


app_name = "wikiSearch"
urlpatterns = [
    path("<str:name>", views.index, name="index"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("search", views.index, name="search")
]