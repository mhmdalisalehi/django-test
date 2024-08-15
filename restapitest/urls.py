from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'restapi'

urlpatterns = [
    path('', views.data_list),
    path('data/<int:pk>/', views.data_detail),
]

