from django.shortcuts import render, redirect
from student.models import Student
from .models import Attendance

def student_attendance(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])
    attendance_data = Attendance.objects.filter(student=student)

    return render(request, "attendance.html", {
        "student": student,
        "attendance_data": attendance_data
    })
