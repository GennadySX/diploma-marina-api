from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model # If used custom user model

from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.response import Response
from .serializers import *


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


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

class ApiLikedView(ListCreateAPIView, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Liked.objects.all()
    serializer_class = LikedSerializer

    def delete(self, request, *args, **kwargs):
        r_id = request.data.get('course_id')
        x_id = request.data.get('user_id')
        db = Liked.objects.filter(course_id=r_id, user_id=x_id)
        if db.exists():
            db.delete()
            return Response({'status': True, 'deleted_id': r_id})
        else:
            return Response({'status': True, 'err': 'object not found'})
       

