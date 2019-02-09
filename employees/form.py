from django import forms
from .models import Employee

class EmployeeCreateForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['full_name', 'emp_id', 'dob', 'date_joined', 'department'] 

        