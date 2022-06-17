from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)
    create_dt = models.DateTimeField('CREATE_DATE', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE_DATE', auto_now=True)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField(max_length=500)
    PhotoFileName = models.CharField(max_length=500)
    create_dt = models.DateTimeField('CREATE_DATE', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE_DATE', auto_now=True)
    