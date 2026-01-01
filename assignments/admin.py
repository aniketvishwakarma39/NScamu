from django.contrib import admin
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'semester', 'section', 'issue_date', 'due_date')
    list_filter = ('semester', 'section', 'subject')

admin.site.register(Assignment, AssignmentAdmin)
