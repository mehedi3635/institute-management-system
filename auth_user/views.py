from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from auth_user.models import CustomeUserModel

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
