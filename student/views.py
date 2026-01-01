from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Student

def student_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pwd = request.POST.get("password")

        try:
            student = Student.objects.get(email=email)

            if check_password(pwd, student.password):
                request.session["student_id"] = student.id
                return redirect("student_profile")
            else:
                return render(request, "login.html", {"error": "Wrong password"})

        except Student.DoesNotExist:
            return render(request, "login.html", {"error": "Student not found"})

    return render(request, "login.html")


def student_logout(request):
    request.session.flush()
    return redirect("student_login")


def student_profile(request):
    if "student_id" not in request.session:
        return redirect("student_login")

    student = Student.objects.get(id=request.session["student_id"])
    return render(request, "profile.html", {"student": student})
