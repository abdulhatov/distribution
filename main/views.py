from django.shortcuts import render
from rest_framework import generics
from .serializers import HumanSerializer
from .models import Human

class HumanCreateView(generics.CreateAPIView):
    serializer_class = HumanSerializer
    queryset = Human.objects.all()
