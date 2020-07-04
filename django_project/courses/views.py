from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Course

class CourseListView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course

class VideoDetailView(View):

    def get(self, request, course_slug, video_slug, *args, **kwargs):

        course_qs = Course.objects.filter(slug=course_slug)
        if course_qs.exists():
            course = course_qs.first()

        video_qs = Course.videos.filter(slug=video_slug)
        if video_qs.exists():
            video = video_qs.first()

        context = {
            'object': video
        }
        return render(request, "video_detail.html", context)