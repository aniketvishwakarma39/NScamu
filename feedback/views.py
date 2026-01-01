from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback
from timetable.models import Subject
from student.models import Student


def give_feedback(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])

    # simple: saare subjects dikha do
    subjects = Subject.objects.filter(semester=student.semester).order_by('name')

    if request.method == "POST":
        for subject in subjects:
            key = f"rating_{subject.id}"
            rating_val = request.POST.get(key)

            if rating_val:
                rating_val = int(rating_val)

                Feedback.objects.update_or_create(
                    student=student,
                    subject=subject,
                    defaults={"rating": rating_val}
                )

        messages.success(request, "Feedback submitted successfully.")
        return redirect('give_feedback')

    return render(request, "feedback_form.html", {
        "student": student,
        "subjects": subjects,
    })
