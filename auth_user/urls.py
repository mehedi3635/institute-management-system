from django.urls import path
from auth_user.views import *


urlpatterns = [
    path('', regeesterpage, name='regeesterpage'),
    path('login/', loginpage, name='loginpage'),
    path('das/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    
    
    path('tea/', teacher, name='teacher'),
    path('r_tea/', reg_teacher, name='reg_teacher'),
    
    
    path('stu/', student, name='student'),
    path('reg_stu/', reg_student, name='reg_student'),
]
