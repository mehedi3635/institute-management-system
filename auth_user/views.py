from django.shortcuts import redirect, render
from auth_user.models import *
# Create your views here.
def regeesterpage(request):
    if request.method =='POST':
      username=  request.post.get('username')
      email=  request.post.get('email')
      psw=  request.post.get('psw')
      psw_repeat=  request.post.get('psw_repeat')
      
      if psw == psw_repeat:
          CustomeUserModel.objects.create_user(
              username=username,
              email=email,
              psw=psw,
              user_type="Admin"
              
          )
          return redirect('loginpage')
    return render(request, 'regerster.html')
    