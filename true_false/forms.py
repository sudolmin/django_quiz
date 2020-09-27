from .models import TF_Question
from django import forms

class AddTFquestionForm(forms.ModelForm):
	class Meta:
		model = TF_Question
		fields = ['quiz','category','sub_category',
		'figure','content','explanation','correct']
		widgets={
			'content':forms.TextInput(attrs={ 'class':'input', 
			'placeholder':'Put your Question here.'}
			),
			'explanation': forms.Textarea(attrs={'class':'input', 
			'placeholder':'Write something explaning the question.',
			'rows':1}
			),
		}