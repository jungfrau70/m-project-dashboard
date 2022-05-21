from django.contrib import admin
from EmployeeApp.models import Departments,Employees

# Register your models here.
@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('DepartmentId', 'update_dt')

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('EmployeeId', 'update_dt')