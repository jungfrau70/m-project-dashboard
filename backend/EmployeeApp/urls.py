from django.conf.urls import url
from EmployeeApp import views

# http://127.0.0.1:8000/employee/ + department/
# http://127.0.0.1:8000/employee/ + department/<int:pk>/
app_name = 'EmployeeApp'
urlpatterns = [
    url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),

    url(r'^employee$', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi),    
]

