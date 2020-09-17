from django.contrib import admin
from account.models import User,Teacher,Student,McqExam,Question,Student_Response
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name","username","email")
    list_filter = ("is_admin","is_teacher")
    search_fields = ("first_name","last_name")
    ordering = ("first_name",)


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    list_display = ("name","username","email")
    list_filter = ("department","subject",)
    search_fields = ("first_name","last_name")
    ordering = ("first_name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("sap_id","name","email")
    list_filter = ("department","division")
    search_fields = ("sap_id",)
    ordering = ("sap_id",)


admin.site.register(McqExam)
admin.site.register(Question)
admin.site.register(Student_Response)
