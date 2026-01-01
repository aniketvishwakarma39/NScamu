from django.shortcuts import render, redirect
from decimal import Decimal
from .models import ExamRegistration
from timetable.models import Subject, TimeTable
from student.models import Student
from fees.models import Fee


def exam_registration(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])

    # is student ke semester + section ke subjects nikaal lo (TimeTable se)
    subjects = Subject.objects.filter(
        timetable__semester=student.semester,
        timetable__section=student.section
    ).distinct().order_by('name')

    # existing registration (agar pehle kiya ho)
    reg, created = ExamRegistration.objects.get_or_create(
        student=student,
        semester=student.semester
    )

    selected_ids = list(reg.subjects.values_list('id', flat=True))

    if request.method == "POST":
        subject_ids = request.POST.getlist("subjects")
        selected_subjects = Subject.objects.filter(id__in=subject_ids)

        # update subjects
        reg.subjects.set(selected_subjects)

        # agar fee add nahi hui aur student ne kuch subject select kiye
        if not reg.fee_added and selected_subjects.exists():
            fee, _ = Fee.objects.get_or_create(
                student=student,
                semester=student.semester,
                defaults={"base_amount": Decimal('0.00')}
            )
            fee.extra_amount += Decimal('1500.00')   # exam course registration fee
            fee.save()

            reg.fee_added = True
            reg.save()

        return redirect('exam_registration')

    return render(request, "exam_registration.html", {
        "student": student,
        "subjects": subjects,
        "selected_ids": selected_ids,
        "reg": reg,
    })
