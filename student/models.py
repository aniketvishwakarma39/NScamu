from django.db import models
from django.contrib.auth.hashers import make_password

class Student(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    father_name = models.CharField(max_length=120, blank=True, null=True)
    mother_name = models.CharField(max_length=120, blank=True, null=True)

    admission_no = models.CharField(max_length=50, blank=True, null=True)
    admission_year = models.CharField(max_length=10, blank=True, null=True)
    roll_no = models.CharField(max_length=50, blank=True, null=True)

    course = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    semester = models.CharField(max_length=20, blank=True, null=True)

    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=80, blank=True, null=True)

    status = models.CharField(max_length=20, default="Active")

    photo = models.ImageField(upload_to="students/", blank=True, null=True)
    section = models.CharField(max_length=10, blank=True, null=True)


    def save(self, *args, **kwargs):
        # password hashing
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
