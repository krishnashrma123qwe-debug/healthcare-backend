from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctor
        fields = (
            'id', 'name', 'specialization', 'phone', 'email',
            'qualification', 'experience_years', 'address',
            'created_by', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def validate_phone(self, value):
        if len(value) < 7:
            raise serializers.ValidationError('Phone number too short.')
        return value
