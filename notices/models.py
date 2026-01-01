from django.db import models

def notice_upload_path(instance, filename):
    return f"notices/{filename}"

class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to=notice_upload_path, blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
