from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    # 1) inafara de parole deoarece ele trebuie redefinite
    # widgets = {
    #     'username': forms.TextInput(attrs={'class': 'outline-none text-emerald-600 font-bold p-2'}),
    #     'email': forms.EmailInput(attrs={'class': 'outline-none text-emerald-600 font-bold p-2'})
    # }
    
    # 2) redefinirea fiecaruui field
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Username...',
        'class': 'outline-none text-emerald-600 font-bold p-2'
        }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Email...',
        'class': 'outline-none text-emerald-600 font-bold p-2'
        }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password...',
        'class': 'outline-none text-emerald-600 font-bold p-2'
        }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password...',
        'class': 'outline-none text-emerald-600 font-bold p-2'
        }))
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Username...',
        'class': 'outline-none text-emerald-600 font-bold p-2'
        }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Password...',
        'class': 'outline-none text-emerald-600 font-bold p-2'
        }))
        
        