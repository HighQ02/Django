from django.urls import path
from .views import *


urlpatterns = [
    path('videos', VideoListView.as_view(), name='videos_list'),
    path('video_detail/<int:pk>', VideoDetailView.as_view(), name='video_detail'),
    path('video_create', VideoCreateView.as_view(), name='vidoe_create'),
    path('video_delete/<int:pk>', VideoDeleteView.as_view(), name='video_delete'),
    path('video_update/<int:pk>', VideoUpdateView.as_view(), name='video_update')
]