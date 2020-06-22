from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', ApiCourseView.as_view()),
    path('lesson/', ApiLessonView.as_view()),
    path('liked/', ApiLikedView.as_view()),
]
