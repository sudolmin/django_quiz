from .models import MCQuestion
from django import forms

class AddMCQuestionForm(forms.ModelForm):
	class Meta:
		model = MCQuestion
		fields = ['quiz','category','sub_category',
		'figure','content','explanation','answer_order']
		widgets={
			'content':forms.TextInput(attrs={ 'class':'input', 
			'placeholder':'Put your Question here.'}
			),
			'explanation': forms.Textarea(attrs={'class':'input', 
			'placeholder':'Write something explaning the question.',
			'rows':1}
			),
		}