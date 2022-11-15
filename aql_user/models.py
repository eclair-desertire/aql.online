from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()

    IS_ACTIVE = (
        (True, 'Не заблокирован'),
        (False, 'Заблокирован'),
    )

    id = models.AutoField(primary_key=True)
    username = models.EmailField('email', max_length=50, default='', unique=True)

    name=models.CharField('Имя',max_length=255,default='',null=True,blank=True)
    surname=models.CharField('Фамилия',max_length=255,default='',null=True,blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        choices=IS_ACTIVE,
        verbose_name='Статус доступа',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.username)
# Create your models here.
