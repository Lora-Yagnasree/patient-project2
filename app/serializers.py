from rest_framework import serializers
from .models import Patient, Identity, Insurance


class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields = ["id", "identity_type", "identity_number"]


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ["id", "insurance_company", "insurance_number"]


class PatientSerializer(serializers.ModelSerializer):
    identities = IdentitySerializer(many=True)
    insurances = InsuranceSerializer(many=True)

    class Meta:
        model = Patient
        fields = '__all__'
    def create(self, validated_data):
        identities_data = validated_data.pop("identities", [])
        insurances_data = validated_data.pop("insurances", [])
        patient = Patient.objects.create(**validated_data)

        for identity_data in identities_data:
            Identity.objects.create(patient=patient, **identity_data)

        for insurance_data in insurances_data:
            Insurance.objects.create(patient=patient, **insurance_data)

        return patient

    def update(self, instance, validated_data):
        identities_data = validated_data.pop("identities", [])
        insurances_data = validated_data.pop("insurances", [])

        # update patient fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # replace old identities
        instance.identities.all().delete()
        for identity_data in identities_data:
            Identity.objects.create(patient=instance, **identity_data)

        # replace old insurances
        instance.insurances.all().delete()
        for insurance_data in insurances_data:
            Insurance.objects.create(patient=instance, **insurance_data)

        return instance

