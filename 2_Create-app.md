WORKDIR="/home/ubuntu/project2/api/DjangoAPI"
cd $WORKDIR

######################################################################
# 1. Create Django App
######################################################################

python manage.py startapp EmployeeApp


######################################################################
# 2. setting.py 에 app 등록
######################################################################


######################################################################
# 3. Create database - mytestdb
######################################################################

(venv) python scripts/create-database.py

######################################################################
# 4. Create tables using ORM
######################################################################

## Register databases in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mytestdb',
        'USER': 'postgres',
        'PASSWORD': 'TldhTl1!',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

## Migrate Models - 실행하면, 마이그래이션 파일이 생성 됨
(venv) python manage.py makemigrations EmployeeApp

# Migrations for 'EmployeeApp':
#   EmployeeApp/migrations/0001_initial.py
#     - Create model Departments
#     - Create model Employees

## Push the changes thru migrations into databases
(venv) python manage.py migrate EmployeeApp

# Operations to perform:
#   Apply all migrations: EmployeeApp
# Running migrations:
#   Applying EmployeeApp.0001_initial... OK

## Check if tables are created
(venv) python scripts/show-tables.py


######################################################################
# 5. Create serializers (convert dataTypes between python and database)
######################################################################

serializers.py


######################################################################
# 6. Write API methods
######################################################################

views.py

## 아래 내용 import 하고,
-. 데이터 변환기 (디비->json) import
-. 정의된 모델 import
-. 정의된 시리얼라이저 import 

## api 만들기