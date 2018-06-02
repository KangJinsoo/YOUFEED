from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from login.models import Userdata, Crawldata
from login.forms import UserdataForm
from django.contrib.auth.models import User

def index(request):
	return render(request, 'ufeed/index.html')

def register(request):
	if request.method == "POST":
		form = UserdataForm(request.POST)
		if form.is_valid():
			userdata = form.save(commit=False)
			userdata.user_id = request.user.id # 구글 접속 user의 pk 받아온 것
			userdata.save()
			return redirect('register')
	else:
		form = UserdataForm()
		return render(request, 'ufeed/register.html', {'form': form})