from django.urls import path
from courses.views import courses

urlpatterns=[
    path('list/',courses.CourseList.as_view({'get':'list'})),
    path('<int:pk>/info/',courses.CourseList.as_view({'get':'retrieve'})),
    path('<int:pk>/delete/',courses.CourseList.as_view({'delete':'destroy'})),
    path('<int:pk>/update/',courses.CourseList.as_view({'put':'partial_update'})),
    path('create/',courses.CourseList.as_view({'post':'create'})),

    path('<int:pk>/add_videos/',courses.Video.as_view({'post':'create'})),
    path('<int:pk>/list_videos/',courses.Video.as_view({'get':'list'})),
    path('video/<int:pk>/view/',courses.Video.as_view({'get':'retrieve'})),
    path('video/<int:pk>/update/',courses.Video.as_view({'put':'partial_update'})),
    path('video/<int:pk>/delete/',courses.Video.as_view({'delete':'destroy'})),

]