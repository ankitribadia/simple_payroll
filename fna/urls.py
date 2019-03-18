from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'attlog', views.AttendanceLogView)
router.register(r'payroll', views.PayrollView)
router.register(r'loanslog', views.LoansView)

urlpatterns = [
    path('', include(router.urls)),
]