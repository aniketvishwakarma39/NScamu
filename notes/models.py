from django.db import models
from timetable.models import Subject

def notes_upload_path(instance, filename):
    return f"notes/{instance.subject.name}/{instance.chapter}/{filename}"

class Notes(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    chapter = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    file = models.FileField(upload_to=notes_upload_path)

    semester = models.CharField(max_length=10)
    section = models.CharField(max_length=10)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject.name} - {self.chapter}"
