from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employeelist', views.ListEmployeesView)
router.register(r'shifts', views.ShiftView)

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.emp_list, name='list'),
    path('create/', views.employee_create, name='create'),
    path('api/', include(router.urls)),
]
