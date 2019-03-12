from django.contrib import admin
from .models import Department, Employee, Shift, Designation

# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Shift)
admin.site.register(Designation)