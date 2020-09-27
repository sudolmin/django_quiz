from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddEssayQuestionForm 

@login_required
def essay(request):
	if request.method == 'POST':
		q_form =AddEssayQuestionForm(request.POST)
		if q_form.is_valid():
			q_form.save()
			messages.success(request, f'Essay Question added successfully.')
			return redirect("quiz_index")
	else:
		q_form =AddEssayQuestionForm()
	context = {
		'q_form': q_form,
	}
	return render(request, 'add.html', context)