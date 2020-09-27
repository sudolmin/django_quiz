from .models import Essay_Question
from django import forms

class AddEssayQuestionForm(forms.ModelForm):
	class Meta:
		model = Essay_Question
		fields = ['quiz','category','sub_category',
		'figure','content','explanation']
		widgets={
			'content':forms.TextInput(attrs={ 'class':'input', 
			'placeholder':'Put your Question here.'}
			),
			'explanation': forms.Textarea(attrs={'class':'input', 
			'placeholder':'Write something explaning the question.',
			'rows':1}
			),
		}