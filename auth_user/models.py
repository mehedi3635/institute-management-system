from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomeUserModel(AbstractUser):
    USER_TYPES={
        ('Admin','Admin'),
        ('Teacher','Teacher'),
        ('Student','Student'),
        
        }
    user_type=models.CharField(choices=USER_TYPES,max_length=10,null=True)
    
    def __str__(self):
        return self.username
    
class TeacherModel(models.Model):
    teacher_user=models.OneToOneField(CustomeUserModel,on_delete=models.CASCADE, null=True,related_name='teacher_info')
    teacher_name=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=29,null=True)
    profile_picture=models.ImageField(upload_to='media/teacher/',null=True)
    
    def __str__(self):
        return self.teacher_name
    

class StudentModel(models.Model):
    student_user=models.OneToOneField(CustomeUserModel,on_delete=models.CASCADE, null=True,related_name='teacher_info')
    student_name=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=29,null=True)
    profile_picture=models.ImageField(upload_to='media/student/',null=True)
    
    def __str__(self):
        return self.student_name