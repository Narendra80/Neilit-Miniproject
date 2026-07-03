from django import forms
from django.contrib.auth.models import User
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'role', 'department', 'salary', 'phone', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Sarah Jenkins'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g. sarah.j@company.com'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Senior Frontend Engineer'}),
            'department': forms.Select(choices=[
                ('Engineering', 'Engineering'),
                ('IT', 'IT & Infrastructure'),
                ('HR', 'Human Resources'),
                ('Finance', 'Finance & Accounting'),
                ('Marketing', 'Marketing & Sales'),
                ('Operations', 'Operations'),
                ('General', 'General Management'),
            ], attrs={'class': 'form-select'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. +1 (555) 234-5678'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter strong password'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match.")
        return cleaned_data
