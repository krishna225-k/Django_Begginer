from django.db import models

# Create your models here.


class StudentData(models.Model):
    
    student_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    telugu_marks = models.IntegerField()
    hindi_marks = models.IntegerField()
    english_marks = models.IntegerField()
    maths_marks = models.IntegerField()
    science_marks = models.IntegerField()
    social_marks = models.IntegerField()