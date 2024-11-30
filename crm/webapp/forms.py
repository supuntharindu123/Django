from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput,EmailInput

from django import forms

from .models import Record

#register/create user
class createuserform(UserCreationForm):
    class meta:
        model = User
        fields=["Username","Password1","Password2"]

#login
class loginform(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your_name", max_length=100)
    your_pwd = forms.CharField(label="Your_pwd", max_length=100)


class CreateRecord(forms.ModelForm):
    class Meta:
        model = Record
        fields=["first_name", "last_name", "email","phone","address","city","province","country"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':"Enter your First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':"Enter your Last Name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2','placeholder':"Enter your Email"}),
            'phone': forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':"Enter your Phone Number"}),
            'address': forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':"Enter your Address"}),
            'city': forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':"Enter your City"}),
            'province': forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':"Enter your Province"}),
            'country': forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':"Enter your Country"}),
        }

class UpdateRecord(forms.ModelForm):
    class Meta:
        model = Record
        fields=["first_name", "last_name", "email","phone","address","city","province","country"]
        