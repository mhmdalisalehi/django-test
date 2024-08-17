from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'restapi'

urlpatterns = [
    path('', views.DataList.as_view(), name='data_list'),
    path('data/<int:pk>/', views.DataDetail.as_view(), name='data_detail'),
]

