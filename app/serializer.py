from rest_framework import serializers
from app.models import *

class schoolmodelserializer(serializers.ModelSerializer):
    class Meta:
        model=school
        #fields='__all__'
        fields=['sname']
