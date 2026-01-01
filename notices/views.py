from django.shortcuts import render, redirect
from .models import Notice
from student.models import Student
from datetime import date

def student_notices(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])

    notices = Notice.objects.all().order_by('-created_at')

    today = date.today()

    return render(request, "notices.html", {
        "student": student,
        "notices": notices,
        "today": today,
    })
