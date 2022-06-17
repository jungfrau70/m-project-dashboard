### Under the DRF Pattern
### 4th, convert dataTypes between database and python

WORKDIR="/root/p-lens-dashboard"
cd $WORKDIR


######################################################################
# 1. Setup Python environment
######################################################################

pip install --upgrade pip
pip install -r requirements.txt


######################################################################
# 2. Startpoject frontend
######################################################################

django-admin startproject frontend .


######################################################################
# 3. Startapp dashboard
######################################################################

django-admin startapp dashboard


######################################################################
# 4. Configure setting.py 에 app 등록
######################################################################

## Application definition

INSTALLED_APPS = [
    ..,
    'rest_framework',                       # djangorestframework
    'corsheaders',                          # cors
    'dashboard.apps.DashboardConfig',       # app - dashboard
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


######################################################################
# 2. Create index.html
######################################################################

touch index.html