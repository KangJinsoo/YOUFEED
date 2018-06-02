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
			return redirect('modify')
	else:
		form = UserdataForm()
		return render(request, 'ufeed/register.html', {'form': form})

def modify(request):
	userdatas = Userdata.objects.all()
	return render(request, 'ufeed/modify.html', {'userdatas' : userdatas})

def edit(request, pk):
	#userdata = Userdata.objects.filter(pk=pk)
	userdata = get_object_or_404(Userdata, pk=pk)
	if request.method == "POST":
		form = UserdataForm(request.POST, instance=userdata)
		if form.is_valid():
			userdata = form.save(commit=False)
			userdata.user_id = request.user.id
			userdata.save()
			return redirect('modify')
	else:
		form = UserdataForm(instance=userdata)
		return render(request, 'ufeed/register.html', {'form': form})

def delete(request, pk):
	userdata = get_object_or_404(Userdata, pk=pk)
	userdata.delete()
	return redirect('modify')

def all_userdata_delete(request):
	userdata = Userdata.objects.all()
	userdata.delete()
	return redirect('modify')

def all_crawldata_delete(request):
	crawldata = Crawldata.objects.all()
	crawldata.delete()
	return redirect('notify')

def notify(request):
	return render(request, 'ufeed/notify.html')

def set_data(request):
	return render(request, 'ufeed/set_data.html')