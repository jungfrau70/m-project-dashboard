### Under the MVT Pattern
### Second, design URLs

WORKDIR="~/coc-dashboard/backend"
cd $WORKDIR

######################################################################
# 1. Design URLs
######################################################################

URL Pattern               View Name               Template FileName
/admin/                   (장고 기본 제공)
/                         HomeView(TemplateView)  home.html
/blog/post/list/          PostLV(ListView)        post_list.html
/blog/post/<int:pk>/      PostDV(DetailView)      post_detail.html


######################################################################
# 2. Design Root(=Project) URLs
######################################################################

from . import views

urlpatterns = [
    ...
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    path('employee/', include('EmployeeApp.urls')),
]


######################################################################
# 3. Design (blog) App URLs
######################################################################

from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('post/list/', views.PostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDV.as_view(), name='post_detail'),
]


######################################################################
# 4. Design (EmployeeApp) App URLs
######################################################################

from django.urls import path
from EmployeeApp import views

app_name = 'EmployeeApp'
urlpatterns = [
    path('employee/list/', views.EmployeAppLV.as_view(), name='employee_list'),
    path('employee/<int:pk>/', views.EmployeeAppDV.as_view(), name='employee_detail'),
]

