from django.db import models
from decimal import Decimal

# Create your models here.


class AbstractBaseModel(models.Model):
    """AbstractBaseModel contains common fields between models.
    All models should extend this class.
    """

    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        abstract = True


class Department(AbstractBaseModel):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department


class Shift(models.Model):
    shift_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    time_start = models.CharField(max_length=5)
    time_end = models.CharField(max_length=5)
    shift_duration = models.CharField(max_length=5)
    shift_month_duration = models.CharField(max_length=5)

    def __str__(self):
        return self.shift_name


class Designation(AbstractBaseModel):
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


zero = Decimal('0.00')


class Employee(AbstractBaseModel):
    full_name = models.CharField(max_length=200, unique=True)
    emp_id = models.IntegerField(default=0)
    dob = models.DateField(blank=True)
    date_joined = models.DateField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=9, decimal_places=2, default=zero)

    def __str__(self):
        return (self.full_name)

