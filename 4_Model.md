### Under the MVT Pattern
### First, create tables

WORKDIR="/root/coc-dashboard/backend"
cd $WORKDIR

######################################################################
# 1. Define tables using models.py
######################################################################

## Blog App
vi blog/models.py

## Employee App
vi EmployeeApp/models.py


######################################################################
# 2. Define tables in Admin site
######################################################################

## Blog App
vi blog/admin.py

## Employee App
vi EmployeeApp/admin.py


######################################################################
# 3. Make migration files
######################################################################

## 실행하면, 마이그래이션 파일이 생성 됨
(venv) python manage.py makemigrations

<!-- You are trying to add the field 'create_dt' with 'auto_now_add=True' to departments without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>> 
You are trying to add the field 'create_dt' with 'auto_now_add=True' to employees without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>> 
Migrations for 'EmployeeApp':
  EmployeeApp/migrations/0002_auto_20220521_1814.py
    - Add field create_dt to departments
    - Add field update_dt to departments
    - Add field create_dt to employees
    - Add field update_dt to employees
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
     -->


<!-- ## Push the changes thru migrations into databases
(venv) python manage.py migrate EmployeeApp

# Operations to perform:
#   Apply all migrations: EmployeeApp
# Running migrations:
#   Applying EmployeeApp.0001_initial... OK -->


######################################################################
# 4. Apply migration files to database
######################################################################

## 실행하면, 데이터베이스에 마이그래이션 파일(수정사항)이 적용 됨
(venv) python manage.py migrate

<!-- Operations to perform:
  Apply all migrations: EmployeeApp, admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying EmployeeApp.0002_auto_20220521_1814... OK
  Applying blog.0001_initial... OK -->


######################################################################
# 5. Check if tables are created
######################################################################

## Check if tables are created
(venv) python ../scripts/select-tables.py


######################################################################
# 6. Check if tables are created
######################################################################

## run django server
(venv) python manage.py runserver

## Admin page
http://127.0.0.1:8000/admin
