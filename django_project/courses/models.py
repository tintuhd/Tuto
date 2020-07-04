from django.db import models

class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

class Video(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    postion = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title