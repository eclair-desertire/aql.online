from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from courses import serializers
from courses.models import Course, CourseVideos
from rest_framework.permissions import AllowAny, IsAuthenticated
from aql_user.permissions import IsSuperAdmin,IsCourseOwner,IsRegular

class CourseList(ModelViewSet):
    permission_classes=[AllowAny,]
    serializer_class=serializers.CourseListSerializer
    queryset=Course.objects.all()

    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['GET'],
        tags=['Courses']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['GET'],
        tags=['Courses']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
class CourseOwnerView(ModelViewSet):
    permission_classes=[
        IsAuthenticated,
        IsCourseOwner
    ]
    serializer_class=serializers.CourseListSerializer
    queryset=Course.objects.all()
    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['POST'],
        tags=['Courses']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['PUT'],
        tags=['Courses']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['DELETE'],
        tags=['Courses']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class VideoView(ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=serializers.CourseVideoSerializer
    queryset=CourseVideos.objects.all()

    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['POST'],
        tags=['Course Video']
    )# TODO Change
    def create(self, request,pk, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['GET'],
        tags=['Course Video']
    )# TODO Change
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['GET'],
        tags=['Course Video']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['PUT'],
        tags=['Course Video']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


    @extend_schema(
        request=serializer_class,
        responses={200: serializer_class},
        methods=['DELETE'],
        tags=['Course Video']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class UserComments(ModelViewSet):
    pass
