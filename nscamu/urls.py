"""
URL configuration for nscamu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('attendance/', include('attendance.urls')),
    path("timetable/", include("timetable.urls")),
    path("marks/", include("marks.urls")),
    path("assignments/", include("assignments.urls")),
    path("holidays/", include("holidays.urls")),
    path("notices/", include("notices.urls")),
    path("notes/", include("notes.urls")),
    path('feedback/', include('feedback.urls')),
    path("fees/", include("fees.urls")),
    path("exam-registration/", include("examreg.urls")),




    




]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
