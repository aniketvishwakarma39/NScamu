from django.db import models
from student.models import Student
from timetable.models import Subject


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    semester = models.CharField(max_length=10)
    internal_marks = models.IntegerField(default=0)
    external_marks = models.IntegerField(default=0)
    total_marks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_marks = self.internal_marks + self.external_marks
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - Sem {self.semester} - {self.subject.name}"


class Result(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    cgpa = models.FloatField(default=0)
    grade = models.CharField(max_length=5, blank=True)
    total_semesters = models.IntegerField(default=1)

    def __str__(self):
        return f"Result - {self.student.name}"
