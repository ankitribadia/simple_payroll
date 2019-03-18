from rest_framework import serializers
from .models import AttendanceLog, PayrollLog, LoansLog


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


class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollLog
        fields = (
            'empId',
            'empName',
            'shiftId',
            'payMonth',
            'payYear',
            'salary',
            'hourlyRate',
            'totalWorkDuration',
            'totalPayout',
            'loan',
            'netSalary',
            'paidOff'
        )


class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoansLog
        fields = (
            'empId',
            'credit',
            'debit',
            'entryDate'
        )