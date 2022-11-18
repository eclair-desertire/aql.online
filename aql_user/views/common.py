from aql_user import serializers
from aql_user.serializers import TokenObtainPairSerializer, TokenRefreshSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework import status, generics
from drf_spectacular.utils import extend_schema
from aql_user.models import User
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
import jwt

class TokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer

class LogoutFormView(APIView):
    permission_classes=[AllowAny,]
    serializer_class=serializers.UserSerializer
    
    @extend_schema(
        responses={200: serializer_class},
        methods=['GET']
    )
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class RegisterUserView(ModelViewSet):
    permission_classes=[AllowAny]
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer

    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['POST'],
        tags=['User Registration']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['POST'],
        tags=['Email Confirmation']
    )
    def request_token(self, request, *args, **kwargs):
        user_data=request.data
        user=User.objects.get(email=user_data['email'])
        print(user)
        token=RefreshToken.for_user(user).access_token
        print(token)
        
        current_site=get_current_site(request).domain
        relariveLink=reverse('email_verify')
        link="http://"+current_site+relariveLink+"?token="+str(token)
        html = render_to_string('mail_body.html', context={'user': user,'token':token,'link':link})
        plain_message=strip_tags(html)

        send_mail(
            subject='Confirm your email '+str(user),
            message=link,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user],
            fail_silently=False,
            html_message=html
        )
        return Response({'status':'email sended'}, status=status.HTTP_201_CREATED)
    


class VerifyEmail(generics.GenericAPIView):
    def get(self,request):
        token=request.GET.get('token')
        try:
            payload=jwt.decode(token,settings.SECRET_KEY)
            user=User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active=True
                user.save()
            return Response({'email':'Successfully activated'},status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as e:
            return Response({'error':' Activation link is expired'},status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            return Response({'error':'Invalid token, request new one'},status=status.HTTP_400_BAD_REQUEST)


class SelfView(ModelViewSet):
    permission_classes=[AllowAny,]
    queryset=User.objects.all()
    serializer_class=serializers.UserSerializer

    @extend_schema(
        responses={200: serializer_class},
        methods=['GET'],
        tags=['Self Information']
    )
    def get(self,request):
        serializer=serializers.UserSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)