### settings.py # 프로젝트에 필요한 설정과 구성 정보
### __init__.py # 빈 파일로, python프로젝트 또는 모듈
### asgi.py     # asgi 호환 웹서버들의 entrypoint
### wsgi.py     # wsgi 호환 웹서비들의 entrypoint
### urls.py     # 프로젝트에 사용되는 url 들의 decorations
### manage.py   # 장고 프로젝트 커멘드라인 유틸리티

WORKDIR="/root/coc-lens/backend"
cd $WORKDIR

######################################################################
# 1. Create Django App
######################################################################

python manage.py startapp EmployeeApp
python manage.py startapp blog

######################################################################
# 2. Configure setting.py 에 app 등록
######################################################################

## Application definition

INSTALLED_APPS = [
    ..,
    'rest_framework',                       # djangorestframework
    'corsheaders',                          # cors
    'blog.apps.BlogConfig',                 # app - blog
    'EmployeeApp.apps.EmployeeappConfig'    # app - Employee
]

## Development mode only
ALLOWED_HOSTS = []


## Configure Project template direcotory, and created folder - templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]

## Configure time-zone - 장고가 TZ 에 따라 시간을 자동 계산해서 보여 주도록 설정 (이때, 디비는 UTC 사용 함)
TIME_ZONE = 'Asia/Seoul'
USE_TZ = True


## Configure static files directory
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

