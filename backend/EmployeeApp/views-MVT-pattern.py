from django.shortcuts import render
from django.views.generic import ListView, DetailView

# http://127.0.0.1:8000/employee/list/
class EmployeeAppLV(ListView):
    model = Employees
    template_name = 'employee_list.html'     # 디폴드 값으로 생략 가능

# http://127.0.0.1:8000/employee/<int:pk>/
class EmployeeAppDV(DetailView):
    model = Employees
    template_name = 'employee_detail.html'   # 디폴트 설정 값으로 생략 가능
