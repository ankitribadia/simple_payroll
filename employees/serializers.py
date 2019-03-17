from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "full_name",
            'emp_id',
            'dob',
            'date_joined',
            'department',
            'shift',
            'salary'
        )