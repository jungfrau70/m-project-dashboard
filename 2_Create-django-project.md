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
mkdir api
cd api

## 프로젝트 생성
django-admin startproject DjangoAPI

### __init__.py # 빈 파일로, python프로젝트 또는 모듈
### asgi.py     # asgi 호환 웹서버들의 entrypoint
### wsgi.py     # wsgi 호환 웹서비들의 entrypoint
### urls.py     # 프로젝트에 사용되는 url 들의 decorations
### settings.py # 프로젝트에 필요한 설정과 구성 정보

### manage.py   # 장고 프로젝트 커멘드라인 유틸리티

######################################################################
# 3. Start project
######################################################################
python manage.py runserver