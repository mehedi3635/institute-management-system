from django.urls import path
from auth_user.views import *


urlpatterns = [
    path('', regeesterpage, name='regeesterpage'),
    path('login/', loginpage, name='loginpage'),
    path('das/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]
