from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from login.models import Profile, Userdata, Crawldata
from django import forms
from django.forms import PasswordInput

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'username': None
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password'] # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'username': None
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date')

class UserdataForm(forms.ModelForm):
    class Meta:
        model = Userdata
        fields = ('key','url')
        widgets = {
            'key': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'})
        }


class CrawldataForm(forms.ModelForm):
    class Meta:
        model = Crawldata
        fields = ('title','url')
