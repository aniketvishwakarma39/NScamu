from django.db import models
from student.models import Student

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    present = models.IntegerField(default=0)
    absent = models.IntegerField(default=0)

    @property
    def percentage(self):
        total = self.present + self.absent
        if total == 0:
            return 0
        return round((self.present / total) * 100, 2)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"
