from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'yourUsername',
                                'label':'Username'
                                }))
    password = forms.CharField(max_length=60,
                               widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'password',
                                }))

    class Meta:
        model = User 
        fields = ['username', 'email']


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'yourUsername',
                                }))
    
    email = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'email',
                                }))
    
    password1 = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'password1',
                                }))
    
    password2 = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'password2',
                                }))
    
    course = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'course',
                                }))
    
    school = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'school',
                                }))

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1','password2']
