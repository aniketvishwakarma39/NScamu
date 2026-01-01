from django.urls import path
from . import views

urlpatterns = [
    path("", views.holidays_view, name="holidays"),
]
