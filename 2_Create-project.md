### settings.py # 프로젝트에 필요한 설정과 구성 정보
### __init__.py # 빈 파일로, python프로젝트 또는 모듈
### asgi.py     # asgi 호환 웹서버들의 entrypoint
### wsgi.py     # wsgi 호환 웹서비들의 entrypoint
### urls.py     # 프로젝트에 사용되는 url 들의 decorations
### manage.py   # 장고 프로젝트 커멘드라인 유틸리티

WORKDIR="~/coc-dashboard/"
cd $WORKDIR

######################################################################
# 1. Create python venv with dependencies
######################################################################

sudo apt-get install python3-venv
python3 -m venv venv --copies
source venv/bin/activate

cat <<EOF | tee requirements.txt
django
djangorestframework
django-cors-headers
psycopg2
EOF

pip install --upgrade pip
pip install -r requirements.txt 


######################################################################
# 2. Create project
######################################################################

mkdir backend frontend
cd backend

## 현재 디렉토리에 프로젝트 생성
django-admin startproject DjangoAPI .


######################################################################
# 3. Create Database - postgresql
######################################################################

### settings.py # 프로젝트에 필요한 설정과 구성 정보

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
(venv) python manage.py migrate

<!-- Operations to perform:
  Apply all migrations: EmployeeApp, admin, auth, contenttypes, sessions
Running migrations:
  Applying EmployeeApp.0001_initial... OK
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK -->


######################################################################
# 4. Create Admin account
######################################################################

(venv) python manage.py createsupersuer

<!-- Username (leave blank to use 'root'): admin
Email address: inhwan.jung@gmail.com
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully. -->


######################################################################
# 5. Start project
######################################################################
python manage.py runserver

Ctrl + C