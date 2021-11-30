from django.shortcuts import render, redirect
from .models import StudentData


# Create your views here.
def home(request):
    students = StudentData.objects.all()
    context = {'students': students}
    return render(request, 'students/home.html', context)


def add_student(request):
    return render(request, 'student/add_student.html')


def save_data(request):
    '''Note: While passing the data from html browser to the database i.e comes to mapping. NO need to give separator "comma(,)"'''
    sname = request.POST.get('sname')
    school = request.POST.get('school')
    cls = request.POST.get('cls')
    section = request.POST.get('section')
    email = request.POST.get('email')
    mobile = request.POST.get('mob')
    telugu = request.POST.get('telugu')
    hindi = request.POST.get('hindi')
    english = request.POST.get('english')
    maths = request.POST.get('maths')
    science = request.POST.get('maths')
    social = request.POST.get('social')
    print(mobile)
    type(mobile)

    data = StudentData(
        student_name=sname,
        school_name=school,
        class_name=cls,
        section=section,
        email=email,
        mobile=mobile,
        telugu_marks=telugu,
        hindi_marks=hindi,
        english_marks=english,
        maths_marks=maths,
        science_marks=science,
        social_marks=social
        )
    data.save()
    return redirect('/')


def student_view(request):
    return render(request, 'students/add_student.html')


def update_data(request,pk):
    student = StudentData.objects.get(id=pk)
    context = {'student':student}
    return render(request,'students/update_data.html', context)


def save_update_data(request,pk):
    student = StudentData.objects.get(id=pk)
    
    student.student_name = request.POST.get('sname')
    student.school_name = request.POST.get('school')
    student.class_name = request.POST.get('cls')
    student.section = request.POST.get('section')
    student.email = request.POST.get('email')
    student.mobile = request.POST.get('mobile')
    student.telugu_marks = request.POST.get('telugu')
    student.hindi_marks = request.POST.get('hindi')
    student.english_marks = request.POST.get('english')
    student.maths_marks = request.POST.get('maths')
    student.science_marks = request.POST.get('science')
    student.social_marks = request.POST.get('social')
    
    student.save()
    return redirect('/')


def delete_data(request, pk):

    student = StudentData.objects.get(id=pk)
    student.delete()
    return redirect('/')
