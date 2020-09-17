from django.contrib import admin
from django.urls import path,include
from account import views

app_name='account'

urlpatterns=[
    path('register/',views.student_register,name='student_register'),
    path('teacher_register/',views.teacher_register,name='teacher'),
    path('login/',views.user_login,name='user_login'),
    path('teacher_list/',views.ChapterListView.as_view(),name='list'),
    path('teacher_list/<int:pk>/',views.QuestionDetailView.as_view(),name='detail'),
    path('addquestion/',views.questionform_view,name='add'),
    path('update/<int:pk>/',views.QuestionUpdateView.as_view(),name='update'),
    path('create/',views.ChapterCreateView.as_view(),name='create'),
    path('student/<int:student_pk>/',views.student_chp_lst,name='list_fun'),
    path('student/<int:student_pk>/<int:chp_pk>/',views.question_detail,name='detail_fun'),
]
