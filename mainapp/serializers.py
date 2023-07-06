from rest_framework import serializers

from mainapp.models import(
    Category, Course, CourseSchedule, LearningTechnology, Comment, Publication
)

from django.contrib.auth import get_user_model


User = get_user_model()


class LearningTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningTechnology
        fields = (
            'id', 'name'
        )


class CourseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSchedule
        fields = (
            'id', 'course', 'start_date', 'end_date',
        )


class CourseSerializer(serializers.ModelSerializer):
    course_schedule = CourseScheduleSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = (
            'id', 'user', 'category', 'name', 'description', 'start_date', 
            'end_date', 'price', 'adress', 'additional_info', 'course_schedule',
        )


class CategorySerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'course',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
