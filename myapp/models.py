from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Video(models.Model):
    video_name = models.CharField(null=False, blank=False, max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    about_video = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return str(self.video_name)

    def get_absolute_url(self):
        return reverse('videos_list')