from django.urls import path

from . import views

app_name = 'restapi'

urlpatterns = [
    path('get/', views.getData),
    path('post/', views.postData),
]