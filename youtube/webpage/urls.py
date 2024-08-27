from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home,video_detail,video_feed,channel_detail



urlpatterns = [
    path('youtube/',home,name = "home"),
    path('video_feed/',video_feed, name='video_feed'),
    path('video/<int:pk>/',video_detail, name='video_detail'),
    path('channel/<int:pk>/',channel_detail, name='channel_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
