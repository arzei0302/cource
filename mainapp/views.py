from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect
from .forms import CommentForm, PublicationForm

from mainapp.models import(
    Category, Course, CourseSchedule, LearningTechnology,
    Publication, Comment
)

from mainapp.serializers import(
    CategorySerializer, CourseSerializer, 
    CourseScheduleSerializer, LearningTechnologySerializer, 
    CommentSerializer, PublicationSerializer
    
)

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()                   
    serializer_class = CategorySerializer


class CourseView(ModelViewSet):
    queryset = Course.objects.all()                   
    serializer_class = CourseSerializer


class CourseScheduleView(ModelViewSet):
    queryset = CourseSchedule.objects.all()                   
    serializer_class = CourseScheduleSerializer


class LearningTechnologyView(ModelViewSet):
    queryset = LearningTechnology.objects.all()                   
    serializer_class = LearningTechnologySerializer


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()                   
    serializer_class = CommentSerializer


class PublicationView(ModelViewSet):
    queryset = Publication.objects.all()                   
    serializer_class = PublicationSerializer
