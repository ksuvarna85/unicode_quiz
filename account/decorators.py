from django.core.exceptions import PermissionDenied
from account.models import Student,Teacher

def user_is_student(function):
    def wrap(request, *args, **kwargs):
        entry = request.user.is_student
        if entry :
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def user_is_teacher(function):
    def wrap(request, *args, **kwargs):
        entry = request.user.is_teacher
        if entry :
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

class TeacherRequiredMixin:
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_teacher:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied
