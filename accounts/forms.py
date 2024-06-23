from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'email',
                                'label':'Email'
                                }))
    password = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'password',
                                }))
    class Meta:
        model = User 
        fields = ['email', 'password']


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'username',
                                }))
    email = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'email',
                                }))
    
    location = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'location',
                                }))
    

    password1 = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'password',
                                }))
    
    password2 = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'password',
                                }))
    

    class Meta:
        model = User 
        fields = ['username', 'email', 'location', 'password1','password2']
