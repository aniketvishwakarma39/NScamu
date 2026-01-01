from django.shortcuts import render, redirect
from .models import TimeTable
from student.models import Student

def view_timetable(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])

    timetable = TimeTable.objects.filter(
        semester=student.semester,
        section=student.section
    ).order_by('day', 'start_time')

    return render(request, "timetable.html", {
        "student": student,
        "timetable": timetable,
    })
