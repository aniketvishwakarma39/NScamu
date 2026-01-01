from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_fees, name="student_fees"),
]
