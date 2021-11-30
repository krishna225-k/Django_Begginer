from django.shortcuts import render,redirect
from .models import StudentDetails,Course,Collage,Branch,Location,Institute,StudentMarks
from .forms import StudentDataForm,UserRegisterForm,AddCourse,AddBranch,AddCollage,AddInstitution,AddLocation,AddMarks
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from crispyformapp.decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group


@login_required(login_url='login')
@allowed_users(allowed_roles=['Students'])
def student_data(request):
    form = StudentDataForm()
    context = {'form':form}
    if request.method == "POST":
        form = StudentDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_page')
        else:
            return redirect('data')
    else:
        return render(request, 'crispy/student.html', context)

@login_required(login_url='login')
@admin_only
def fetching_data(request):
    data  = StudentDetails.objects.all()
    context = {'data':data}
    return render(request, 'crispy/studentdata.html', context)

@unauthenticated_user
def register_view(request):
    form = UserRegisterForm()
    context = {'form':form}
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            name1 = request.POST.get('name')
            group = Group.objects.get(name='Students')
            user.groups.add(group)
            StudentDetails.objects.create(
                user=user
            )
            # messages.success(request, 'Account Created Successfully for ' + name1)
            return redirect('login')
    return render(request,'crispy/register.html',context)

@unauthenticated_user
def login_view(request):
    if request.method=="POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(username=username1, password=password1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request, 'Username Or Password Wrong')
    return render(request,'crispy/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def courses_view(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request,'crispy/courses.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def collages_view(request):
    collages = Collage.objects.all()
    context = {'collages':collages}
    return render(request,'crispy/collages.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def locations_view(request):
    locations = Location.objects.all()
    context = {'locations':locations}
    return render(request,'crispy/locations.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def branches_view(request):
    branches = Branch.objects.all()
    context = {'branches':branches}
    return render(request,'crispy/branches.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def institutions_view(request):
    institutions = Institute.objects.all()
    context = {'institutions':institutions}
    return render(request,'crispy/institutions.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def add_course(request):
    form = AddCourse()
    context = {'form':form}
    if request.method == "POST":
        form = AddCourse(request.POST)
        if form.is_valid():
            name1 = request.POST.get('name')
            form.save()
            messages.success(request,name1 + 'Course is added successfully ')
            return redirect('courses')
    return render(request,'crispy/adding.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def add_collage(request):
    form = AddCollage()
    context = {'form':form}
    if request.method == "POST":
        form = AddCollage(request.POST)
        if form.is_valid():
            name1 = request.POST.get('name')
            form.save()
            messages.success(request,name1 + 'Collage is added successfully ')
            return redirect('collages')
    return render(request, 'crispy/adding.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def add_location(request):
    form = AddLocation()
    context = {'form':form}
    if request.method == "POST":
        form = AddLocation(request.POST)
        if form.is_valid():
            name1 = request.POST.get('name')
            form.save()
            messages.success(request,name1 + ' location is added successfully ')
            return redirect('locations')
    return render(request, 'crispy/adding.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def add_branch(request):
    form = AddBranch()
    context = {'form':form}
    if request.method == "POST":
        form = AddBranch(request.POST)
        if form.is_valid():
            name1 = request.POST.get('name')
            form.save()
            messages.success(request,name1 + ' branch is added successfully ')
            return redirect('branches')
    return render(request, 'crispy/adding.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def add_institute(request):
    form = AddInstitution()
    context = {'form':form}
    if request.method == "POST":
        form = AddInstitution(request.POST)
        if form.is_valid():
            name1 = request.POST.get('name')
            form.save()
            messages.success(request,name1 + ' branch is added successfully ')
            return redirect('institutions')
    return render(request, 'crispy/adding.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def update_course(request,pk):
    course = Course.objects.get(id=pk)
    form = AddCourse(instance=course)
    context = {'form':form}
    if request.method == "POST":
        form = AddCourse(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    return render(request, 'crispy/updating.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def update_collage(request,pk):
    collage = Collage.objects.get(id=pk)
    form = AddCollage(instance=collage)
    context = {'form':form}
    if request.method == "POST":
        form = AddCollage(request.POST,instance=collage)
        if form.is_valid():
            form.save()
            return redirect('collages')
    return render(request, 'crispy/updating.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def update_location(request,pk):
    location = Location.objects.get(id=pk)
    form = AddLocation(instance=location)
    context = {'form':form}
    if request.method == "POST":
        form = AddLocation(request.POST,instance=location)
        if form.is_valid():
            form.save()
            return redirect('locations')
    return render(request, 'crispy/updating.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def update_branch(request,pk):
    branch = Branch.objects.get(id=pk)
    form = AddBranch(instance=branch)
    context = {'form':form}
    if request.method == "POST":
        form = AddBranch(request.POST,instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branches')
    return render(request, 'crispy/updating.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def update_institute(request,pk):
    institute = Institute.objects.get(id=pk)
    form = AddInstitution(instance=institute)
    context = {'form':form}
    if request.method == "POST":
        form = AddInstitution(request.POST,instance=institute)
        if form.is_valid():
            form.save()
            return redirect('institutions')
    return render(request, 'crispy/updating.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def delete_course(request,pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('courses')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def delete_collage(request,pk):
    collage = Collage.objects.get(id=pk)
    collage.delete()
    return redirect('collages')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def delete_location(request,pk):
    location = Location.objects.get(id=pk)
    location.delete()
    return redirect('locations')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def delete_branch(request,pk):
    branch = Branch.objects.get(id=pk)
    branch.delete()
    return redirect('branches')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admins'])
def delete_institute(request,pk):
    institute = Institute.objects.get(id=pk)
    institute.delete()
    return redirect('institutions')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Students'])
def student_page(request):
    students = StudentDetails.objects.all()
    marks = StudentMarks.objects.all()
    context = {'students':students,'marks':marks}
    return render(request,'crispy/student_page.html',context)


def no_entry(request):
    return render(request,'crispy/no_entry.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Students'])
def add_marks(request):
    if request.method == "POST":
        form = AddMarks(request.POST,request.FILES)
        if form.is_valid():
            telugu1 = request.POST.get('telugu')
            hindi = request.POST.get('hindi')
            maths1 = request.POST.get('maths')
            english1 = request.POST.get('english')
            science1 = request.POST.get('science')
            social1 = request.POST.get('social')

            total_marks = int(telugu1)+int(hindi)+int(english1)+int(maths1)+int(science1)+int(social1)
            avarage_marks = int(total_marks)/6
            percentage = (int(total_marks)/600)*100

            data = StudentMarks(
                telugu=telugu1,
                hindi=hindi,
                maths=maths1,
                english=english1,
                science=science1,
                social= social1,
                total_marks=total_marks,
                avarage_marks=avarage_marks,
                percentage=round(percentage,2)
            )
            data.save()
            return redirect('fetch_marks')
        else:
            return redirect('fetch_marks')
    else:
        form = AddMarks()
        context = {'form': form}
        return render(request,'crispy/add_marks.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Students'])
def fetch_marks(request):
    marks = StudentMarks.objects.all()
    context = {'marks':marks}
    return render(request,'crispy/display_marks.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Students'])
def modify_data(request):
    form = StudentDataForm()
    context = {'form':form}
    return render(request,'crispy/modify_marks.html',context)
