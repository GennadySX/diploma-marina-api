from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import  redirect
from django.http import HttpResponse
from django.template import RequestContext
from .models import *
from rest_framework import generics
from .serializers import *
import json

# Create your views here.


class ApiCourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ApiLessonView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class ApiLikedView(generics.ListCreateAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedSerializer
