from django.contrib import admin
from .models import Student
from django.utils.html import format_html
from django.contrib.auth.hashers import make_password

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'roll_no',
        'course',
        'semester',
        'section',        # <-- ADDED
        'status',
        'photo_preview'
    )

    search_fields = ('name', 'email', 'roll_no', 'course')
    list_filter = ('course', 'semester', 'section', 'status')   # <-- ADDED

    # fields used in admin form (so section appears during add/edit)
    fields = (
        'name', 'email', 'password',
        'father_name', 'mother_name',
        'admission_no', 'admission_year', 'roll_no',
        'course', 'branch', 'semester', 'section',   # <-- ADDED HERE
        'address', 'city', 'state',
        'status', 'photo'
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width="50" style="border-radius:6px;">')
        return "No Photo"
