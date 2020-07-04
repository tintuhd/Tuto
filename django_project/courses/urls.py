from django.urls import path
from .views import CourseListView, CourseDetailView, VideoDetailView
app_name = 'courses'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('<slug>', CourseDetailView.as_view(), name='detail'),
    path('<course_slug>/<video_slug>', VideoDetailView.as_view(), name='video-detail')

]