from django.shortcuts import render

from .models import Employee
# Create your views here.
def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {'employees': employees})

def home(request):
    return render(request, 'home.html')