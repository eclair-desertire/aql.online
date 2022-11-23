from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet
class CourseList(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)