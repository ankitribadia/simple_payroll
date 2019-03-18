from django.shortcuts import render
from rest_framework import viewsets

from .models import AttendanceLog
from .serializers import AttendanceSerializer


# Create your views here.
class AttendanceLogSerializer(viewsets.ModelViewSet):
    queryset = AttendanceLog.objects.all()
    serializer_class = AttendanceSerializer
