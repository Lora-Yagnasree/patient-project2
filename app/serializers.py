from rest_framework import serializers
from .models import Patient
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    IDENTITY_TYPE_CHOICES = ['Aadhar No','PAN','Passport','Driving License','Voter ID','Other']
    INSURANCE_CHOICES = ['HDFC ERGO','ICICI Lombard','Bajaj Allianz','Star Health','Other']
    def validate_identities(self, value):
        for entry in value:
            if 'identity_type' not in entry or 'identity_number' not in entry:
                raise serializers.ValidationError("Each identity must have type and number.")
            if entry['identity_type'] not in self.IDENTITY_TYPE_CHOICES:
                raise serializers.ValidationError(f"Invalid identity_type: {entry['identity_type']}")
        return value
    def validate_insurance(self, value):
        if value is None:
            return []  # default to empty list if nothing sent
        for entry in value:
            if 'insurance_company' not in entry or 'insurance_number' not in entry:
                raise serializers.ValidationError("Each insurance must have company and number.")
            if entry['insurance_company'] not in self.INSURANCE_CHOICES:
                raise serializers.ValidationError(f"Invalid insurance_company: {entry['insurance_company']}")
        return value

