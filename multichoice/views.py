from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddMCQuestionForm 
from .models import MCQuestion, Answer
from django.forms.models import inlineformset_factory, modelformset_factory

@login_required
def mcq(request):
	if request.method == 'POST':
		
		q_form =AddMCQuestionForm(request.POST, request.FILES)
		Answerformset = inlineformset_factory(MCQuestion, Answer, 
			fields = ('content','correct'),  max_num=4)
		if q_form.is_valid():
			obj=q_form.save()
			a_form = Answerformset(request.POST, instance=obj)
			if a_form.is_valid():
				a_form.save()
				messages.success(request, f'MCQuestion added successfully.')
				return redirect("quiz_index")
	else:
		q_form =AddMCQuestionForm()
		Answerformset = inlineformset_factory(MCQuestion, Answer, 
			fields = ('content','correct'), extra=4,  max_num=4)
		a_form = Answerformset()
	context = {
		'q_form': q_form,
		'a_form': a_form,
	}
	return render(request, 'add.html', context)