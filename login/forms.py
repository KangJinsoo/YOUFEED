from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from login.models import Profile, Userdata, Crawldata
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

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
            'url': forms.TextInput(attrs={'class': 'form-control'})
        }


class CrawldataForm(forms.ModelForm):
    class Meta:
        model = Crawldata
        fields = ('title','url')
