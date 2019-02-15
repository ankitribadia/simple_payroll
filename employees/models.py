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


zero = Decimal('0.00')


class Employee(AbstractBaseModel):
    full_name = models.CharField(max_length=200)
    emp_id = models.IntegerField(default=0)
    dob = models.DateField(blank=True)
    date_joined = models.DateField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=9, decimal_places=2, default=zero)

    def __str__(self):
        return (self.full_name)