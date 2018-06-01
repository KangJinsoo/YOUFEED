from django import forms
from .models import Userdata

class UserdataForm(forms.ModelForm):

	class Meta:
		model = Userdata
		fields = ('key','url',)