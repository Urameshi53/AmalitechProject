from django.contrib.auth.models import User 
from rest_framework import serializers

from .models import School, AccessKey

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School 
        fields = ['url', 'school_name', 'email', 'id', 'accesskey_set']

class KeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccessKey
        fields = ['url', 'key_encrypted', 'key_plain', 'school', 'date_proc', 'date_exp']
