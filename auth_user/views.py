from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from auth_user.models import *
from django.contrib import messages


def regeesterpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        psw_repeat = request.POST.get('psw_repeat')

        if password != psw_repeat:
            return render(request, 'regerster.html', {'error': 'Passwords do not match'})

        # Optional: check if username exists
        if CustomeUserModel.objects.filter(username=username).exists():
            return render(request, 'regerster.html', {'error': 'Username already exists'})

        CustomeUserModel.objects.create_user(
            username=username,
            email=email,
            password=password,
            user_type="Admin"
        )
        return redirect('loginpage')

    return render(request, 'regerster.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('loginpage')

# teacher section
def teacher(request):
     teachers = TeacherModel.objects.all()
     
     context={
         'teachers':teachers
     }
     return render(request, 'teacher.html',context)
def reg_teacher(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        teacher_name = request.POST.get('teacher_name')
        email = request.POST.get('email')
        
        phone_number = request.POST.get('phone_number')
        profile_picture = request.FILES.get('profile_picture')
        
        user_data= CustomeUserModel.objects.create_user(
            username=username,
            email=email,
            password=phone_number,
            user_type="Teacher"
        )
        if user_data:
            TeacherModel.objects.create(
                teacher_user=user_data,
                teacher_name=teacher_name,
                phone_number=phone_number,
                profile_picture=profile_picture,
            )
            return redirect('teacher')
        
     return render(request, 'regester_teacher.html')


def student(request):
    students = StudentModel.objects.all()

    context = {
        'students': students
    }
    return render(request, 'student.html',context)

def reg_student(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        # username unique check
        if CustomeUserModel.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('reg_student')

        student_name = request.POST.get('student_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        profile_picture = request.FILES.get('profile_picture')

        # create user
        user_data = CustomeUserModel.objects.create_user(
            username=username,
            email=email,
            password=phone_number,   # temporary password
            user_type="Student"
        )

        # create student profile
        StudentModel.objects.create(
            student_user=user_data,
            student_name=student_name,
            phone_number=phone_number,
            profile_picture=profile_picture,
        )

        messages.success(request, 'Student registered successfully')
        return redirect('student')

    return render(request, 'regester_student.html')


