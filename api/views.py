from rest_framework import generics
from .serializers import *
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

class ApiInitView(generics.ListCreateAPIView):
    queryset = Lesson.objects.filter(course_id=1)
    serializer_class = CourseSerializer

class ApiCourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ApiLessonView(generics.ListCreateAPIView):
    queryset = Lesson.objects.prefetch_related().all()
    serializer_class = LessonSerializer

class ApiLikedView(generics.ListCreateAPIView):
    queryset = Liked.objects.all()
    serializer_class = LikedSerializer
