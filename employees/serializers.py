from rest_framework import serializers
from .models import Employee, Shift


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


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = (
            'shift_name',
            'description',
            'breakAllowed',
            'time_start',
            'time_end',
            'shift_duration',
            'shift_duration',
            'shift_month_duration'
        )