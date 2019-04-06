from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from python_api import textClearing
from .serializers import VideoSerializer
from .models import Video

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    http_method_names = ['get', 'post']
