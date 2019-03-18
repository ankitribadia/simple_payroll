# from django.shortcuts import render
from rest_framework import viewsets

from .models import AttendanceLog, PayrollLog, LoansLog
from .serializers import AttendanceSerializer, PayrollSerializer, LoansSerializer


# Create your views here.
class AttendanceLogView(viewsets.ModelViewSet):
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceSerializer


class PayrollView(viewsets.ModelViewSet):
    queryset = PayrollLog.objects.all()
    serializer_class = PayrollSerializer


class LoansView(viewsets.ModelViewSet):
    queryset = LoansLog.objects.all()
    serializer_class = LoansSerializer
