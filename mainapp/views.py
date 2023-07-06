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



def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comment_success')
    else:
        form = CommentForm()
    
    return {'form': form}

def create_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.user = request.user
            publication.save()
            return redirect('publication_success')
    else:
        form = PublicationForm()

    return {'form': form}

