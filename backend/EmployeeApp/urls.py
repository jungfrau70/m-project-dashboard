from django.urls import path
from EmployeeApp import views

app_name = 'EmployeeApp'
urlpatterns = [
    path('employee/list/', views.EmployeAppLV.as_view(), name='employee_list'),
    path('employee/<int:pk>/', views.EmployeeAppDV.as_view(), name='employee_detail'),
]