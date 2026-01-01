from django.db import models
from student.models import Student
from timetable.models import Subject

def assignment_upload_path(instance, filename):
    return f"assignments/{instance.semester}/{instance.section}/{filename}"

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    file = models.FileField(upload_to=assignment_upload_path)

    issue_date = models.DateField()
    due_date = models.DateField()

    semester = models.CharField(max_length=10)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title} - {self.subject.name}"
