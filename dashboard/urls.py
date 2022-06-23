from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('dashboard/', views.IndexView.as_view(), name='dashboard'),
]
