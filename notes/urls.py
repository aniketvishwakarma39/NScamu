from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_notes, name="student_notes"),
]
