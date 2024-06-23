from datetime import timezone
from typing import Any, Dict
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from django.views import generic
from django.template import RequestContext
from django.views.generic.base import RedirectView
from django import urls

from .forms import LoginForm, RegistrationForm
from tenant.models import School
from django.contrib.auth import logout


class ProfileView(generic.DetailView):
    template_name = "accounts/profile.html"
    model = School

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['school'] = School.objects.filter(user=self.request.user)[0]

        return context

def login(request):
    form = LoginForm
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        #user = authenticate(request, email=email, password=password)
        user = None
        for i in User.objects.all():
            if i.email == email:# and i.check_password(password):
                user = i
                
        if user is not None:
            auth_login(request, user)

            if user.is_superuser:
                #urls(r'^$', RedirectView.as_view(url='/admin'))
                #return redirect(url)
                return redirect('admin')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Username or password does not match')
            print('did not work')
    else:
        pass    

    return render(request, 'accounts/login.html', {'form':form})#, RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    form = RegistrationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        location = request.POST.get('location')
        password1 = request.POST.get('password1')
        password1 = request.POST.get('password1')

        user = User()
        user.username = username
        user.email = email
        user.password = password1
        user.save()

        school = School()
        school.user_id = user.id
        school.school_name = user.username
        school.email = user.email
        school.password = password1
        school.save()

        auth_login(request, user)

        return redirect('home')
    else:
        pass    

    return render(request, 'accounts/signup.html', {'form':form})