from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_timetable, name="student_timetable"),
]
