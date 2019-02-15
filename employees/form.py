from django import forms

from .models import Employee

# for adding datepicker


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeCreateForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            'full_name', 'emp_id', 'dob', 'date_joined', 'department', 'salary'
            ]
        labels = {
            'dob': 'Date of Birth'
        }
        widgets = {
            'dob': DateInput(),
            'date_joined': DateInput()
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save'))
