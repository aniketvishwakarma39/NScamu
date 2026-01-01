from django.contrib import admin
from .models import Holiday

class HolidayAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    list_filter = ('start_date',)

admin.site.register(Holiday, HolidayAdmin)
