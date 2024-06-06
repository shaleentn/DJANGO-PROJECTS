from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Faculty, Department
from .models import Resource


class SignUpForm(UserCreationForm):
    faculty = forms.ModelChoiceField(queryset=Faculty.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    staff_id = forms.CharField(required=False, help_text="Enter Staff ID if you are a lecturer")

    class Meta:
        model = User
        fields = ('username', 'faculty', 'department', 'staff_id', 'password1', 'password2')

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'file', 'description']