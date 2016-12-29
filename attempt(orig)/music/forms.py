from django import forms

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'text','placeholder':'Password'}))
    #confirmpassword = forms.CharField(widget=forms.PasswordInput)
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'text','placeholder':'First name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'text','placeholder':'last name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'text','placeholder':'Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','type':'text','placeholder':'Email'}))
    class Meta:
        model = User
        fields = ['firstname' , 'lastname','username', 'email', 'password'  ]
