from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_assignments, name="student_assignments"),
]
