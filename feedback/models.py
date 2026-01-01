from django.db import models
from student.models import Student
from timetable.models import Subject


class Feedback(models.Model):
    RATING_CHOICES = (
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'subject')  # ek student ek subject ko ek baar hi rate kare

    @property
    def percentage(self):
        # 5 star = 100%, 1 star = 20%
        return self.rating * 20

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.rating}★"
