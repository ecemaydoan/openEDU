from django.db import models

# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=200, unique=True, verbose_name="Course name",help_text="Enter the course name")
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to="courses/%Y/%m/%d/")
    date=models.DateTimeField(auto_now=True)
    available=models.BooleanField(default=True)


