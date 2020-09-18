from django.shortcuts import render,redirect
from account.forms import StudentForm,TeacherForm,QuestionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from account import models
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from account.decorators import user_is_student,TeacherRequiredMixin,user_is_teacher
from django.utils.decorators import method_decorator
# Create your views here.

def index(request):
    return render(request,'account/index.html')

#def student_register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        student_form=StudentForm(data=request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()


            registered=True

        else:
            print(user_form.errors,student_form.errors)

    else:
        user_form=UserForm()
        student_form=StudentForm()

    return render(request,'account/student.html',{'user_form':user_form,
                                                    'student_form':student_form,
                                                    'registered':registered})
def student_register(request):
    registered=False
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            role = form.cleaned_data.get('role')
            #user = authenticate(username=username, password=raw_password)
            print(role)
            login(request, user)
            registered=True
    else:
        form = StudentForm()
    return render(request, 'account/student.html', {'form': form,
                                                    'registered':registered})


def teacher_register(request):
    registered=False
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            role = form.cleaned_data.get('role')
            #user = authenticate(username=username, password=raw_password)
            print(role)
            login(request, user)
            registered=True
    else:
        form = TeacherForm()
    return render(request, 'account/teacher.html', {'form': form,'registered':registered})


def user_login(request):

    if request.method=="POST":

        email=request.POST.get('email')
        password=request.POST.get('Password')
        test=request.POST.get('is_teacher')
        student_pk=models.User.objects.get(email=email).id
        #student_pk=models.Student.objects.get(id=request.user)
        print(student_pk)
        print(test)
        user=authenticate(email=email,password=password)


        if user:
            if user.is_active:
                login(request,user)
                if request.user.is_teacher:
                    return redirect('account:list')
                else:
                    return redirect('account:list_fun',student_pk)

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED")
    else:
        return render(request,'account/user_login.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class ChapterListView(LoginRequiredMixin,TeacherRequiredMixin,ListView):
    model=models.McqExam


class QuestionDetailView(LoginRequiredMixin,TeacherRequiredMixin,DetailView):
    context_object_name='question'
    model=models.McqExam
    template_name='account/quiz_detail.html'

@login_required
@user_is_teacher
def questionform_view(request):
    form=QuestionForm()
    if request.method=="POST":
        form=QuestionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('account:list')

    return render(request,'account/question.html',{'form':form})

class QuestionUpdateView(LoginRequiredMixin,TeacherRequiredMixin,UpdateView):
    fields=('id','question','option_1','option_2','option_3','option_4','correct_ans')
    model=models.Question


class ChapterCreateView(LoginRequiredMixin,TeacherRequiredMixin,CreateView):
    fields=('exam_topic',)
    model=models.McqExam

@login_required
@user_is_student
def student_chp_lst(request,student_pk):
    topic=models.McqExam.objects.all()
    return render(request,'account/student_chp_lst.html',{'topic':topic,'student_pk':student_pk})

@login_required
@user_is_student
def question_detail(request,chp_pk,student_pk):

    if request.method=='POST':

        answer=request.POST.get('ans')
        question=request.POST.get('luck')

        question=models.Question.objects.get(id=question)
        student_email=models.Student.objects.get(email=request.user)

        student_response=models.Student_Response(student_response=answer,question=question,student=student_email)


        student_response.save()



        return redirect('account:detail_fun',student_pk,chp_pk)

    else:
        questions=models.Question.objects.filter(mcq_exam=chp_pk)

        return render(request,'account/detail.html',{'questions':questions,})


class ChapterDeleteView(LoginRequiredMixin,TeacherRequiredMixin,DeleteView):
    model=models.McqExam
    success_url=reverse_lazy('account:list')
