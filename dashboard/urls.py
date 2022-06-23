from django.urls import path

from dashboard.views import IndexView

app_name="apps"

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
]