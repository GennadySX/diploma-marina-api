from rest_framework import serializers
from api.models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'desc',
            'avatar',
            'created_at',
            'status',
        )
        model = Course


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'course_id',
            'name',
            'desc',
            'avatar',
            'video',
            'created_at',
            'status',
        )
        model = Lesson


class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'course_id',
            'user_id',
            'desc',
        )
        model = Liked
