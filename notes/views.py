from django.shortcuts import render, redirect
from .models import Notes
from student.models import Student

def student_notes(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])

    notes = Notes.objects.filter(
        semester=student.semester,
        section=student.section
    ).order_by('subject__name', 'chapter')

    return render(request, "notes.html", {
        "student": student,
        "notes": notes,
    })
