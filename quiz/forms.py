from django import forms
from quiz.models import Question

class QuestionForm(forms.ModelForm):
    class Meta():
        model=Question
        fields=('mcq_exam','question','option_1','option_2','option_3','option_4','correct_ans')
