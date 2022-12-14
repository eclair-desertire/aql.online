from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer, TokenObtainPairSerializer
)
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from .models import User
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


class TokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, *args, **kwargs):
        data = super().validate(*args, **kwargs)

        if not self.user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {self.user.email} был деактивирован!"
            }, code='user_deleted')

        data['id'] = self.user.id
        data['email'] = self.user.email

        return data

class TokenRefreshSerializer(TokenRefreshSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])

        try:
            user = User.objects.get(
                pk=refresh.payload.get('user_id')
            )
        except ObjectDoesNotExist:
            raise serializers.ValidationError({
                'detail': f"Пользователь был удалён!"
            }, code='user_does_not_exists')

        if not user.is_active:
            raise AuthenticationFailed({
                'detail': f"Пользователь {user.email} был архивирован!"
            }, code='user_deleted')

        data['id'] = user.id
        data['email'] = user.email

        access = AccessToken(data['access'])

        return data

class Pagination(PageNumberPagination):

    class Meta:
        ordering = ['-id']

    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page': self.page.number,
            'results': data
        })

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('id','email','password','role','name','surname','is_active','is_email_confirmed')
        extra_kwargs={
            'name':{'required':False},
            'surname':{'required':False},
            'is_active':{'required':False},
            'is_email_confirmed':{'required':False},
            'role':{'required':False}
        }

    def save(self):
        password = self.validated_data.pop('password', None)
        if password:
            self.validated_data['password'] = make_password(password)

        return super().save()

    def password_save(self,new_password):
        self.validated_data['password']=make_password(new_password)

        return super().save()


class PasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField()
    old_password_confirm=serializers.CharField()
    new_password=serializers.CharField()