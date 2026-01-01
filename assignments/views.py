from django.shortcuts import render, redirect
from .models import Assignment
from student.models import Student
from datetime import date

def student_assignments(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])

    assignments = Assignment.objects.filter(
        semester=student.semester,
        section=student.section
    ).order_by('-issue_date')

    today = date.today()

    return render(request, "assignments.html", {
        "student": student,
        "assignments": assignments,
        "today": today
    })
