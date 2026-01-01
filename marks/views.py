from django.shortcuts import render, redirect
from .models import Mark, Result
from student.models import Student

def student_marks(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])

    # Fetch all semesters for this student
    semesters = Mark.objects.filter(student=student).values_list('semester', flat=True).distinct()

    # Marks grouped by semester
    marks_data = {}
    for sem in semesters:
        marks_data[sem] = Mark.objects.filter(student=student, semester=sem)

    return render(request, "marks.html", {
        "student": student,
        "marks_data": marks_data,
        "semesters": semesters,
    })


def student_result(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])
    result = Result.objects.filter(student=student).first()

    return render(request, "result.html", {
        "student": student,
        "result": result
    })
