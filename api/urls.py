from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/',  CreateUserView.as_view()),
    path('all/', ApiLessonView.as_view()),
    path('course/', ApiCourseView.as_view()),
    path('lesson/', ApiLessonView.as_view()),
    path('liked/', ApiLikedView.as_view()),
    path('account/', CurrentUserView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
