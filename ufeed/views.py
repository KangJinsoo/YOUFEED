from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from login.models import Userdata, Crawldata
from login.forms import UserdataForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'ufeed/index.html')

@login_required
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

@login_required
def modify(request):
	#userdatas = Userdata.objects.all()
	id = request.user.id
	userdatas = Userdata.objects.filter(user_id=id).order_by('-id')
	if	len(userdatas) == 0:
		return redirect('index')
	return render(request, 'ufeed/modify.html', {'userdatas' : userdatas})

@login_required
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

@login_required
def delete(request, pk):
	userdata = get_object_or_404(Userdata, pk=pk)
	userdata.delete()
	return redirect('modify')

@login_required
def all_userdata_delete(request):
	userdata = Userdata.objects.all()
	userdata.delete()
	return redirect('modify')

@login_required
def all_crawldata_delete(request):
	crawldata = Crawldata.objects.all()
	crawldata.delete()
	return redirect('notify')

@login_required
def notify(request):
	#crawldatas = Crawldata.objects.all()
	id = request.user.id
	crawldatas = Crawldata.objects.filter(user_id=id).order_by('-id')
	if	len(crawldatas) == 0:
		return redirect('index')

	return render(request, 'ufeed/notify.html', {'crawldatas' : crawldatas})

@login_required
def set_data(request):
	return render(request, 'ufeed/set_data.html')
