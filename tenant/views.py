from typing import Any, Dict
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.core.paginator import Paginator
# Create your views here.



class IndexView(generic.TemplateView):
    template_name = 'tenant/index.html'