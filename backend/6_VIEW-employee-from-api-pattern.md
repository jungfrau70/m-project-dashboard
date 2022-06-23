### Under the MVT Pattern
### 4th, create VIEWs

(방법1) DRF(API) 패턴
#### 1. crsf_exempt 는 다른 도메인에서 api 를 접근할 수 있게 해 줌
#### 2. JSONParser 는 incoming data 를 data model 로 Parsing
#### 3. Model import
#### 4. Serializer import
#### 5. api 생성

WORKDIR="/root/coc-lens/backend"
cd $WORKDIR


######################################################################
# 1. (Prereq) Create Serializer
######################################################################

GOTO 8_SERIALIZER.md first

######################################################################
# 2. Create EmployeeApp view
######################################################################

### 아래 모듈 import 하여, api 생성
### 1. crsf_exempt 는 다른 도메인에서 api 를 접근할 수 있게 해 줌
### 2. 데이터 변환기 (database->python[json]->database) import
###    JSONParser 는 incoming data 를 data model 로 Parsing
### 3. 정의된 모델 import
### 4. 정의된 시리얼라이저 import 
### 5. api 생성

cat <<EOF | tee EmployeeApp/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

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
EOF

