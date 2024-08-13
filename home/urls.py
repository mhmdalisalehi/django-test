from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('products/',views.products,name='product'),
    path('details/<slug>/<int:id>',views.product_details,name='details'),
    path('category/<slug>/<int:id>',views.products,name='category'),
    path('navbar/',views.navbar,name='navbar'),
]