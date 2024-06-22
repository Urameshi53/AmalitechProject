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


class IndexView(generic.TemplateView):
    template_name = 'tenant/index.html'

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
