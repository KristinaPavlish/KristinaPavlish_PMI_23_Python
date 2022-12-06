import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.http import Http404
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Patients


def validate_only_letter(string):
    if (any(x.isalpha() for x in string)
            and any(x.isspace() for x in string)
            and all(x.isalpha() or x.isspace() for x in string)):
        raise ValidationError(
            '%(value)s is not an even number', params={'string': string}, )


class PatientSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField()
    name = serializers.SlugField(max_length=200, required=True)
    date = serializers.DateField()
    time = serializers.TimeField()
    duration = serializers.IntegerField()
    doctor_name = serializers.SlugField(max_length=200, required=True)
    department = serializers.SlugField(max_length=200, required=True)



    class Meta:
        model = Patients
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Students` instance, given the validated data.
        """
        return Patients.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Patients` instance, given the validated data.
        """

        instance.patient_id = validated_data.get('id', instance.patient_id)
        instance.name = validated_data.get('patient_name', instance.patient_name)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.doctor_name = validated_data.get('doctor_name', instance.doctor_name)
        instance.department = validated_data.get('department', instance.department)

        instance.save()
        return instance
