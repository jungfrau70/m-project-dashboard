from django.urls import path
from EmployeeApp import views

# http://127.0.0.1:8000/employee/ + list/
# http://127.0.0.1:8000/employee/ + <int:pk>/
app_name = 'EmployeeApp'
urlpatterns = [
    path('list/', views.EmployeeAppLV.as_view(), name='employee_list'),
    path('<int:pk>/', views.EmployeeAppDV.as_view(), name='employee_detail'),
]

