from rest_framework import serializers
from api.models import *
from rest_framework.serializers import *
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Lesson


class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Liked


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    liked = LikedSerializer(many=True, read_only=True)

    class Meta:
        fields = "__all__"
        model = Course


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", 'first_name', 'last_name', 'email' )