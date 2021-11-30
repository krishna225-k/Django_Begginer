from django.db import models
from django.contrib.auth.models import User

class Collage(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Branch(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Institute(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Location(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class StudentMarks(models.Model):
    telugu = models.IntegerField()
    hindi = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    social = models.IntegerField()
    total_marks = models.IntegerField(default=0)
    avarage_marks = models.IntegerField(default=0)
    percentage = models.FloatField(default=0)
    # profile_pic = models.ImageField(upload_to='images/',default='pic.jpeg')


class StudentDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    student = models.OneToOneField(StudentMarks, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField(null=True,blank=True)
    fee = models.IntegerField()
    collage = models.ForeignKey(Collage,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
