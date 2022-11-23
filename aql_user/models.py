from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .managers import UserManager
from django.utils.translation import gettext as _

class User(AbstractBaseUser, PermissionsMixin):

    SUPERADMIN, COURSEOWNER, REGULAR = range(1,4)
    
    objects = UserManager()

    ROLE_GROUP={
        SUPERADMIN:1,
        COURSEOWNER:2,
        REGULAR:3,
    }

    ROLE_TYPES={
        (SUPERADMIN, _('SUPERADMIN')),
        (COURSEOWNER, _('COURSEOWNER')),
        (REGULAR, _('REGULAR')),
    }

    IS_ACTIVE = (
        (True, 'Не заблокирован'),
        (False, 'Заблокирован'),
    )

    id = models.AutoField(primary_key=True)
    image=models.FileField('Аватар',upload_to='media/users/avatar/',null=True, blank=True)
    email = models.EmailField('email', max_length=50, default='', unique=True)
    role=models.IntegerField('Роль',choices=ROLE_TYPES,default=REGULAR)
    name=models.CharField('Имя',max_length=255,default='',null=True,blank=True)
    surname=models.CharField('Фамилия',max_length=255,default='',null=True,blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        choices=IS_ACTIVE,
        verbose_name='Статус доступа',
    )
    is_email_confirmed=models.BooleanField(
        default=False,
        verbose_name="Почта подтверждена"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.email)+" - "+str(self.role)
# Create your models here.
