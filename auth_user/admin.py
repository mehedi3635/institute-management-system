from django.contrib import admin

from auth_user.models import *

# Register your models here.
admin.site.register(CustomeUserModel)
admin.site.register(TeacherModel)
admin.site.register(StudentModel)