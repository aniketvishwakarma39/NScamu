from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'rating', 'percentage', 'created_at')
    list_filter = ('subject', 'rating')
    search_fields = ('student__name', 'subject__name')
    ordering = ('-created_at',)
