from django.shortcuts import render, redirect
from decimal import Decimal
from .models import Fee
from student.models import Student


def student_fees(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])

    fees = Fee.objects.filter(student=student).order_by('semester')

    total_due = sum((f.due_amount for f in fees), Decimal('0.00'))

    # agar future me advance payment / credit rakhna ho to yahan change kar sakte ho
    credit_balance = Decimal('0.00')

    context = {
        "student": student,
        "fees": fees,
        "total_due": total_due,
        "credit_balance": credit_balance,
    }
    return render(request, "fees.html", context)
