from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['student_id', 'student_name', 'gender', 'dob', 'phone_number', 'email']