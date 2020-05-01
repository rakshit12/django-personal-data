
from django.urls import path, include
from . import views
app_name='blog'
urlpatterns = [
    path('', views.all_fold, name='all_fold'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
