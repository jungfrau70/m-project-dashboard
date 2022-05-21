from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

# http://127.0.0.1:8000/employee/list/
class EmployeeAppLV(ListView):
    model = Employees
    template_name = 'employee_list.html'     # 디폴드 값으로 생략 가능

# http://127.0.0.1:8000/employee/<int:pk>/
class EmployeeAppDV(DetailView):
    model = Employees
    template_name = 'employee_detail.html'   # 디폴트 설정 값으로 생략 가능

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.object.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully")
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.object.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")