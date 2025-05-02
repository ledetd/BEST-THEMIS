from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name = "note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),

    path("projects/", views.ProjectListCreate.as_view(), name = "project-list"),
    path("projects/delete/<int:pk>/", views.ProjectDelete.as_view(), name = "delete-project"),
]