from django.db import models
from student.models import Student
from timetable.models import Subject


class ExamRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    subjects = models.ManyToManyField(Subject, blank=True)

    fee_added = models.BooleanField(default=False)  # 1500 extra fee already added or not
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Exam Reg - {self.student.name} - Sem {self.semester}"
