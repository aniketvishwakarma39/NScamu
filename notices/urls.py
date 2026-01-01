from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_notices, name="student_notices"),
]
