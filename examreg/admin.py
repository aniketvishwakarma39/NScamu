from django.contrib import admin
from .models import ExamRegistration

@admin.register(ExamRegistration)
class ExamRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'created_at', 'fee_added')
    filter_horizontal = ('subjects',)
    list_filter = ('semester', 'fee_added')
