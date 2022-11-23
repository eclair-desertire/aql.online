from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from courses import serializers
from courses.models import Course
class CourseList(ModelViewSet):
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