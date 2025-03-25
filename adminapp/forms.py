from django import forms
from home.models import *


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class GuruhForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "category": forms.Select(attrs={'class': 'form-control'}),  # To‘g‘ri maydon
            "title": forms.TextInput(attrs={'class': 'form-control'}),  # To‘g‘ri maydon
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "cost": forms.NumberInput(attrs={'class': 'form-control'}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
            "img": forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            "customer": forms.Select(attrs={'class': 'form-control'}),
            "address": forms.Textarea(attrs={'class': 'form-control'}),  # To‘g‘ri maydon
            "payment_type": forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # To‘g‘ri maydon
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "phone": forms.NumberInput(attrs={'class': 'form-control'}),
        }


class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = "__all__"
        widgets = {
            "order": forms.Select(attrs={'class': 'form-control'}),
            "product": forms.Select(attrs={'class': 'form-control'}),
            "count": forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            "price": forms.NumberInput(attrs={'class': 'form-control'}),
        }
