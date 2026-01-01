from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_marks, name="student_marks"),
    path("result/", views.student_result, name="student_result"),
]
