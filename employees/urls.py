from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.emp_list, name='list'),
    path('create/', views.employee_create, name='create'),
]
