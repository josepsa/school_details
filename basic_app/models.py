from django.db import models

# Create your models here.
from django.urls import reverse


class School(models.Model):
    name=models.CharField(max_length=256)
    principal=models.CharField(max_length=256)
    location=models.CharField(max_length=256)
    def __str__(self):
        return self.name
    def get_absolute_url(self):  ##This is where the page redirects when new school is successfully added
        return reverse("basic_app:details",kwargs={'pk':self.pk})

class Students(models.Model):
    student_name=models.CharField(max_length=256)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(School,related_name='Students',on_delete=models.CASCADE)  ##related name is used in html
    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse("basic_app:student_form_success")