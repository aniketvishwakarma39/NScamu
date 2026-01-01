from django.contrib import admin
from .models import Attendance, Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "present", "absent", "percentage")
    list_filter = ("subject",)
    search_fields = ("student__name", "subject__name")
