### Under the DRF Pattern
### 4th, convert dataTypes between database and python

WORKDIR="/root/coc-lens/backend"
cd $WORKDIR


######################################################################
# 1. Convert dataTypes between python and database, and then render to json type, etc
######################################################################

cat <<EOF | tee EmployeeApp/serializers.py
from rest_framework import serializers
from EmployeeApp.models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId', 'DepartmentName', 'create_dt', 'update_dt')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName', 'create_dt', 'update_dt')

