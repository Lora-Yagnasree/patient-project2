from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
     # <-- this ensures full URL

    class Meta:
        model = Patient
        fields = '__all__'

