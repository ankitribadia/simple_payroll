from django.shortcuts import render, redirect
from rest_framework import viewsets


from .form import EmployeeCreateForm
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
def emp_list(request):
    context = {
        "title": "Directory",
        'employees': Employee.objects.all()
    }
    return render(request, 'list.html', context)


def home(request):
    return render(request, 'home.html')


def employee_create(request):
    form = EmployeeCreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('list')

    context = {
        "title": "Create Employee",
        "form": form
    }
    return render(request, "employee/create.html", context)


# adding the api view of employee
class ListEmployeesView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer