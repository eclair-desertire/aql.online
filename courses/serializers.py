from rest_framework import serializers
from .models import Course, CourseComments, CourseProgress, CourseVideoProgress, CourseVideos

# Main Serializers
class CourseVideoProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model=CourseVideoProgress
        fields=('__all__')
class CourseProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model=CourseProgress
        fields=('__all__')

class CourseCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model=CourseComments
        fields=('__all__')

class CourseVideoSerializer(serializers.ModelSerializer):
    comments=CourseCommentsSerializer(many=True)
    video_progress=CourseVideoProgressSerializer(many=True)


    class Meta:
        model=CourseVideos
        fields=('module','image','title','description',
        'materials','video','comments','video_progress',)


class CourseSerializer(serializers.ModelSerializer):
    videos=CourseVideoSerializer(many=True)
    course_progress=CourseProgressSerializer(many=True)

    class Meta:
        model=Course
        fields=('id','owner','image','type','title',
        'type','description','videos','course_progress')



# Sub Serializers
class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=('__all__')

