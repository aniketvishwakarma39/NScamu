from django.db import models
from student.models import Student
from decimal import Decimal


class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)

    # basic amounts
    base_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)   # college decide kare
    extra_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # exam fee, fine, etc.
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # optional: due date (agar chaho to admin se set karna)
    due_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_amount(self):
        return (self.base_amount or 0) + (self.extra_amount or 0)

    @property
    def due_amount(self):
        return self.total_amount - (self.amount_paid or 0)

    @property
    def status(self):
        """ UI ke liye status text """
        if self.due_amount <= Decimal('0.00'):
            return "Settled"        # Paid
        if self.amount_paid == 0:
            return "Unpaid"
        return "Partial"            # Partial paid

    def __str__(self):
        return f"{self.student.name} - Sem {self.semester}"
