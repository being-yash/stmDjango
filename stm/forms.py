from django.core import validators
from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['name', 'studentClass', 'rollNo', 'phone', 'email', 'password']
		widgets = {
			'name' : forms.TextInput(attrs={'class':'form-control'}),
			'studentClass' : forms.TextInput(attrs={'class':'form-control'}),
			'rollNo' : forms.TextInput(attrs={'class':'form-control'}),
			'phone' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.EmailInput(attrs={'class':'form-control'}),
			'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
		}