from django import forms
from .models import User, UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="Enter a strong Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        labels = {
            "email": "Enter a stong Email",
        }
        widgets = { "email": forms.EmailInput(attrs={"placeholder": "Enter a strong Email"})}
