from django.shortcuts import render

from .form import EmployeeCreateForm
from .models import Employee


# Create your views here.
def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {'employees': employees})

def home(request):
    return render(request, 'home.html')

def employee_create(request):
    form = EmployeeCreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        employees = Employee.objects.all()
        return render(request, 'list.html', {'employees': employees})
    context = {
        "title" : "Create Employee",
        "form" : form
    }
    return render(request, "employee/create.html", context)