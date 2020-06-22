from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/',  CreateUserView.as_view()),
    path('all/', ApiLessonView.as_view()),
    path('course/', ApiCourseView.as_view()),
    path('lesson/', ApiLessonView.as_view()),
    path('liked/', ApiLikedView.as_view()),
]
