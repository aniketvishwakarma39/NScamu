from django.contrib import admin
from .models import Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ("subject", "chapter", "semester", "section", "created_at")
    list_filter = ("subject", "semester", "section")

admin.site.register(Notes, NotesAdmin)
