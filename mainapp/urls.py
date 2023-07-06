from rest_framework.routers import DefaultRouter as DR

from mainapp.views import(
   CategoryView, CourseView, CourseScheduleView, LearningTechnologyView,
   CommentView, PublicationView
)

router = DR()

router.register('category', CategoryView)
router.register('course', CourseView)
router.register('CourseSchedule', CourseScheduleView)
router.register('LearningTechnology', LearningTechnologyView)

router.register('Comment', CommentView)
router.register('Publication', PublicationView)

urlpatterns = []

urlpatterns += router.urls