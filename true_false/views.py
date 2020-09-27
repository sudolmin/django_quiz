from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddTFquestionForm
from .models import TF_Question

@login_required
def tfq(request):
	if request.method == 'POST':
		
		q_form =AddTFquestionForm(request.POST, request.FILES)
		if q_form.is_valid():
			obj=q_form.save()
			messages.success(request, f'True False added successfully.')
			return redirect("quiz_index")
				
	else:
		q_form =AddTFquestionForm()
	context = {
		'q_form': q_form,
	}
	return render(request, 'add.html', context)
