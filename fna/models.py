from django.db import models
from decimal import Decimal

# Create your models here.


class AttendanceLog(models.Model):
    empId = models.IntegerField()
    empName = models.CharField(max_length=100)
    empDept = models.CharField(max_length=30)
    shiftId = models.IntegerField()
    attDay = models.CharField(max_length=10)
    attMonth = models.CharField(max_length=20)
    attYear = models.CharField(max_length=4)
    attDate = models.DateField(max_length=10)
    timeIn = models.CharField(max_length=5)
    timeOut = models.CharField(max_length=5)
    moveOut = models.CharField(max_length=5)
    moveIn = models.CharField(max_length=5)
    duration = models.CharField(max_length=5)


zero = Decimal('0.00')


class PayrollLog(models.Model):
    empId = models.IntegerField()
    empName = models.CharField(max_length=100)
    shiftId = models.IntegerField()
    payMonth = models.CharField(max_length=20)
    payYear = models.CharField(max_length=4)
    salary = models.DecimalField(max_digits=9, decimal_places=2, default=zero)
    hourlyRate = models.IntegerField()
    totalWorkDuration = models.DecimalField(max_digits=9, decimal_places=2, default=zero)
    totalPayout = models.DecimalField(max_digits=9, decimal_places=2, default=zero)
    loan = models.FloatField(default=0)
    netSalary = models.DecimalField(max_digits=9, decimal_places=2, default=zero)
    paidOff = models.BooleanField(default=False)


class LoansLog(models.Model):
    empId = models.IntegerField()
    credit = models.DecimalField(max_digits=9, decimal_places=2, default=zero)
    debit = models.DecimalField(max_digits=9, decimal_places=2, default=zero)
    entryDate = models.DecimalField(max_digits=9, decimal_places=2, default=zero)
