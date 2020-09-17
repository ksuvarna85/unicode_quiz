from django.contrib import admin
from quiz.models import McqExam,Question,Student_Response

admin.site.register(McqExam)
admin.site.register(Question)
admin.site.register(Student_Response)

# Register your models here.
