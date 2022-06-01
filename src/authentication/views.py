from django.shortcuts import render
from .models import CustomUser, Event
from .serializers import LeadSerializer
from rest_framework import generics

# Create your views here.


class LeadListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LeadSerializer
