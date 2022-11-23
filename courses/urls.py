from django.urls import path
from courses.views import courses

urlpatterns=[
    path('course_list/',courses.CourseList.as_view())
]