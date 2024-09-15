from django.urls import path

from . import views

# app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.show_entry_search, name="search"),
    path("wiki/newentry", views.new_entry, name="newentry"),
    path("wiki/save", views.save, name="save"),
    path("wiki/save_edit", views.save_edit, name="save_edited"),
    path("wiki/edit", views.edit, name="edit"),
    path("wiki/random", views.random_title, name="random"),
    path("wiki/<str:title>", views.show_entry, name="entry")
]
