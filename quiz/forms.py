from django import forms
from django.forms.widgets import RadioSelect, Textarea
from .models import Quiz

class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)


class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(
            widget=Textarea(attrs={'style': 'width:100%'}))

class AddQuizForm(forms.ModelForm):
	class Meta:
		model = Quiz
		fields = ['title','description','url',
		'category','random_order','max_questions','answers_at_end',
		'exam_paper','single_attempt','pass_mark',
		'success_text','fail_text','draft']
		widgets={
			'success_text': forms.Textarea(attrs={'class':'input', 
			'placeholder':'''Write the text displayed when the 
student clears the Quiz/Exam''',
			'rows':2}
			),
			'fail_text': forms.Textarea(attrs={'class':'input', 
			'placeholder':'''Write the text displayed when the 
student FAILS to clear the Quiz/Exam''',
			'rows':2}
			),
			'description': forms.Textarea(attrs={'class':'input', 
			'placeholder':'''Put in some description''',
			'rows':1}
			),
		}