from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms.widgets import RadioSelect
from django.db import transaction
from django.forms.utils import ValidationError

class StudentForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    CHOICES=[('is_student','STUDENT'),('is_teacher','TEACHER')]
    role = forms.CharField(max_length=100,required=True, help_text='STUDENT/TEACHER')

    is_student = forms.BooleanField()



    class Meta:
        model = Student
        fields = ( 'first_name', 'last_name','is_student', 'email', 'password1', 'password2','sap_id','username' )

class TeacherForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    role = forms.CharField(max_length=100, required=True,help_text='STUDENT/TEACHER')
    is_teacher = forms.BooleanField()


    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name','is_teacher', 'email', 'password1', 'password2','username','subject' )

class QuestionForm(forms.ModelForm):
    class Meta():
        model=Question
        fields=('mcq_exam','question','option_1','option_2','option_3','option_4','correct_ans')
