from django.shortcuts import render, redirect
from datetime import date, timedelta
from .models import Holiday
from student.models import Student
import calendar

def holidays_view(request):
    if 'student_id' not in request.session:
        return redirect('student_login')

    student = Student.objects.get(id=request.session['student_id'])

    # All holidays
    holidays = Holiday.objects.all().order_by('-start_date')

    # Calendar data
    today = date.today()
    year = today.year
    month = today.month

    cal = calendar.monthcalendar(year, month)

    # Convert each holiday into list of all dates
    holiday_dates = []

    for h in holidays:
        cur = h.start_date
        while cur <= h.end_date:
            holiday_dates.append(cur)
            cur += timedelta(days=1)

    return render(request, "holidays.html", {
        "student": student,
        "holidays": holidays,
        "calendar": cal,
        "year": year,
        "month": month,
        "holiday_dates": holiday_dates,
    })
