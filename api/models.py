from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Course(models.Model):
    name = models.CharField(verbose_name='Название курса', max_length=225)
    desc = models.TextField(verbose_name='Описание курса', null=True)
    avatar = models.FileField(upload_to='uploads/', verbose_name='Картинка курса', null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Создатель курса', on_delete=models.CASCADE)
    # created_at = models.DateField(verbose_name='Дата создания', default=timezone.now)
    status = models.PositiveIntegerField(default=1, verbose_name='Статус курса', choices=(
        (0, u'Не активен'),
        (1, u'Активен')
    ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course_id = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название урока', max_length=225)
    desc = models.TextField(verbose_name='Описание урока', null=True)
    avatar = models.FileField(upload_to='uploads/', verbose_name='Картинка урока', null=True)
    video = models.FileField(upload_to='uploads/video/', verbose_name='Видео материаль урока', null=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Создатель урока', on_delete=models.CASCADE)
    # created_at = models.DateField(verbose_name='Дата загрузки', default=timezone.now, null=True)
    status = models.PositiveIntegerField(default=1, verbose_name='Статус курса', choices=(
        (0, u'Не активен'),
        (1, u'Активен')
    ))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Liked(models.Model):
    course_id = models.ForeignKey(Course, related_name='liked', on_delete=models.CASCADE, verbose_name='Курс', )
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', verbose_name='Избратель',
                                on_delete=models.CASCADE)
    # created_at = models.DateField(verbose_name='Дата избрание', default=timezone.now)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'
