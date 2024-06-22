from datetime import timezone
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateInput, ModelForm
from django.utils.timezone import now
from django.contrib import admin

from tenant.mother import Mother

mother = Mother()

# Create your models here.
class School(models.Model):
    location = models.CharField(max_length=60, blank=True, default='Kumasi')
    school_name = models.CharField(max_length=60, blank=True, default='KNUST')
    email = models.EmailField(blank=True, default='knust@gmail.com')

    def __str__(self) -> str:
        return self.school_name
    
class AccessKey(models.Model):
    a = mother.generate_key()

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    key_plain = models.CharField(max_length=60, default=a.key_plain)
    key_encrypted = models.CharField(max_length=60, default=a.key_encrypted)
    date_proc = models.DateTimeField()
    date_exp = models.DateTimeField()
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('EXPIRED', 'Expired'),
        ('REVOKED', 'Revoked'),
    )
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=a.status)


    def check_status(self):
        now = timezone.now()
        if now - datetime.timedelta(days=1) <= self.date_proc <= now:
            self.status = 'Active'
        else:
            self.status = 'Expired'

    def __str__(self):
        return self.key_encrypted




