# Generated by Django 4.0 on 2022-11-23 05:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aql_user', '0005_user_image_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(blank=True, null=True, upload_to='media/courses/image/', verbose_name='Обложка Курса')),
                ('title', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Наименование курса')),
                ('type', models.CharField(choices=[('SE', 'Программная инженерия'), ('IS', 'Информационная безопасность'), ('DESIGN', 'Дизайн'), ('GAME', 'Разработка Игр'), ('ML', 'Машинное обучение'), ('CM', 'COMMON_TEST')], default='CM', max_length=255, verbose_name='Тип курса')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание курса')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aql_user.user')),
            ],
        ),
        migrations.CreateModel(
            name='CourseVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.IntegerField(blank=True, default=1, null=True, verbose_name='Модуль')),
                ('image', models.FileField(blank=True, null=True, upload_to='media/course_video/image/', verbose_name='Обложка урока')),
                ('title', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Название урока')),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Описание урока')),
                ('materials', models.FileField(blank=True, null=True, upload_to='media/courses/materials/', verbose_name='Материалы урока')),
                ('video', models.FileField(blank=True, null=True, upload_to='media/courses/videos/', verbose_name='Видеоурок')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Связанный курс')),
            ],
        ),
        migrations.CreateModel(
            name='CourseVideoProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(default='0:00', max_length=255, verbose_name='Длительность')),
                ('completed', models.CharField(default='0:00', max_length=255, verbose_name='Завершено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aql_user.user')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursevideos')),
            ],
        ),
        migrations.CreateModel(
            name='CourseProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aql_user.user')),
            ],
        ),
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aql_user.user')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursevideos', verbose_name='Связанное видео')),
            ],
        ),
    ]