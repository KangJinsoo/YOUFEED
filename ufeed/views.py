from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, 'ufeed/index.html')

def register(request):
	if request.method == "POST":
		form = UserdataForm(request.POST)
		if form.is_valid():
			post = form.save()
			return redirect('modify')
	else:
		form = UserdataForm()
		return render(request, 'ufeed/register.html', {'form': form})