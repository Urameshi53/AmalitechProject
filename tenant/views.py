from typing import Any, Dict
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions

from .models import School, AccessKey
from .serializers import SchoolSerializer, KeySerializer

#key_list = []
#for i in range(10):
#    a = AccessKey()
#    key_list.append(a)

class IndexView(generic.TemplateView):
    template_name = 'tenant/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            context['school'] = School.objects.filter(user=self.request.user)[0]

        return context
    
class KeyDetailView(generic.ListView):
    template_name = 'tenant/key_detail.html'
    model = AccessKey

    def get_queryset(self):
        return AccessKey.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(KeyDetailView, self).get_context_data(*args, **kwargs)
        context['school'] = School.objects.filter(user=self.request.user)[0]
        #context['keys'] = key_list

        keys = AccessKey.objects.filter(school=context['school'])
        other_keys = []
        for key in keys:
            if key.status == 'ACTIVE':
                context['active_key'] = key
            else:
                other_keys.append(key)
                print(key.key_plain)
        context['keys'] = other_keys

        return context



class SchoolViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = School.objects.all()
    serializer_class = SchoolSerializer 
    permission_classes = [permissions.IsAuthenticated]

class KeyViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = AccessKey.objects.all()
    serializer_class = KeySerializer 
    permission_classes = [permissions.IsAuthenticated]
