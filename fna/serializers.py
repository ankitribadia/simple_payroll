from rest_framework import serializers
from .models import AttendanceLog


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceLog
        fields = (
            'empId',
            'empName',
            'empDept',
            'shiftId',
            'attDay',
            'attMonth',
            'attYear',
            'attDate',
            'timeIn',
            'timeOut',
            'moveOut',
            'moveIn',
            'duration'
        )