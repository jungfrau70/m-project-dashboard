from django.urls import path
from blog import views

#     (project url)           + (app url)
# http://127.0.0.1:8000/blog/ + post/list/
# http://127.0.0.1:8000/blog/ + <int:pk>/
app_name = 'blog'
urlpatterns = [
    path('post/list/', views.PostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDV.as_view(), name='post_detail'),
]