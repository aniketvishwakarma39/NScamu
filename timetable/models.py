from django.db import models
from student.models import Student

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True)
    semester = models.CharField(max_length=10, default="1")   # NEW

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class TimeTable(models.Model):
    DAYS = (
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
    )

    day = models.CharField(max_length=20, choices=DAYS)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    semester = models.CharField(max_length=10, default="1")
    section = models.CharField(max_length=10, default="A")

    def __str__(self):
        return f"{self.day} - {self.subject.name}"
