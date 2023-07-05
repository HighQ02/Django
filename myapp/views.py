from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Video


class VideoListView(ListView):
    model = Video
    template_name = 'videos_list_page.html'
    context_object_name = 'Videos'


class VideoDetailView(DetailView):
    model = Video  
    template_name = 'video_detail_page.html'  
    context_object_name = 'Video'


class VideoCreateView(CreateView):
    model = Video
    template_name = 'video_create_page.html'
    fields = ['video_name', 'author', 'about_video']


class VideoDeleteView(DeleteView):
    model = Video
    template_name = 'video_delete_page.html'
    success_url = reverse_lazy('videos_list')


class VideoUpdateView(UpdateView):
    model = Video
    template_name = 'video_update_page.html'
    fields = ['video_name', 'about_video']