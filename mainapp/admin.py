from django.contrib import admin
from mainapp.models import(
    Category, Course, CourseSchedule, LearningTechnology, Comment, Publication
)

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(CourseSchedule)
admin.site.register(LearningTechnology)
admin.site.register(Comment)
admin.site.register(Publication)