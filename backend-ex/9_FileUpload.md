### Under the DRF Pattern
### 4th, convert dataTypes between database and python

WORKDIR="/root/coc-lens/backend"
cd $WORKDIR


######################################################################
# 1. Create folder - Photos
######################################################################

mkdir -p Photos


######################################################################
# 2. Configure in settings.py
######################################################################

## 아래 3개 라인으로 저장 장소 설정
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
MEDIA_URL='/Photos/'
MEDIA_ROOT = os.path.join(BASE_DIR,'Photos')


######################################################################
# 3. Configure API(default storage module) in views.py
######################################################################

from django.core.files.storage import default_storage

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name,safe=False)


######################################################################
# 4. Configure URL
######################################################################

cat <<EOF | tee -a EmployeeApp/urls.py
from django.conf.urls.static import static
from django.conf import settings

app_name = 'EmployeeApp'
urlpatterns = [
    ...

    url(r'^/employee/savefile', views.savefile)
]+static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
EOF

######################################################################
# 5. Check if API works
######################################################################
