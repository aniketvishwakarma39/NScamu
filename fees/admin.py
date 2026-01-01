from django.contrib import admin
from .models import Fee

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'semester', 'base_amount', 'extra_amount', 'amount_paid', 'total_amount', 'due_amount')
    list_filter = ('semester',)
    search_fields = ('student__name', 'student__id')
