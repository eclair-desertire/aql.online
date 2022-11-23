from django.db import models
from django.conf import settings
from django.utils import timezone
from aql_user.models import User

class Course(models.Model):

    COURSE_TYPES=(
        ('SE','Программная инженерия'),
        ('IS','Информационная безопасность'),
        ('DESIGN','Дизайн'),
        ('GAME','Разработка Игр'),
        ('ML','Машинное обучение'),
        ('CM','COMMON_TEST')
    )

    id=models.AutoField(primary_key=True)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image=models.FileField('Обложка Курса',upload_to='media/courses/image/',null=True, blank=True)
    type=models.CharField('Тип курса',max_length=255,null=True,blank=True)
    title=models.CharField('Наименование курса',default='',max_length=255,null=True,blank=True)
    type=models.CharField('Тип курса',default='CM',choices=COURSE_TYPES,max_length=255)

    description=models.TextField('Описание курса',default='',null=True,blank=True)

    


class CourseVideos(models.Model):
    
    course=models.ForeignKey(Course,verbose_name='Связанный курс',on_delete=models.CASCADE)

    module=models.IntegerField('Модуль',default=1,null=True,blank=True)
    image=models.FileField('Обложка урока',upload_to='media/course_video/image/',null=True, blank=True)
    title=models.CharField('Название урока',max_length=255,null=True,blank=True,default='')
    description=models.CharField('Описание урока',max_length=255,null=True,blank=True,default='')
    materials=models.FileField('Материалы урока',upload_to='media/courses/materials/',null=True,blank=True)

    video=models.FileField('Видеоурок',upload_to='media/courses/videos/',null=True, blank=True)

class CourseVideoProgress(models.Model):
    video=models.ForeignKey(CourseVideos, on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    duration=models.CharField('Длительность',max_length=255,default='0:00')
    completed=models.CharField('Завершено',max_length=255,default='0:00')

class CourseProgress(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class CourseComments(models.Model):
    video=models.ForeignKey(CourseVideos,verbose_name='Связанное видео', on_delete=models.CASCADE)

    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text=models.TextField('Комментарий')

    published_date=models.DateTimeField(default=timezone.now)



# Create your models here.
