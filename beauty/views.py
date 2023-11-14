from django.shortcuts import render
from rest_framework import generics
from .models import Beauty
from .serializers import BeautySerializer


class BeautyView(generics.ListAPIView):
    queryset = Beauty.objects.all()
    serializer_class = BeautySerializer


class BeautyCreate(generics.CreateAPIView):
    queryset = Beauty.objects.all()
    serializer_class = BeautySerializer

