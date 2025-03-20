from django import forms
from .models import *


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }



class GuruhForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        widgets = {
            "faculty": forms.Select(attrs={'class': 'form-control'}),
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})

        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
        }


