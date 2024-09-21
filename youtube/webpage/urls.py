from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import video_detail,video_feed,add_video,channel_detail,like_video,LoginPage,HomePage,LogoutPage,SignupPage,add_comment,like_comment



urlpatterns = [
    path('',SignupPage,name='signup'),
    path('login/',LoginPage,name='login'),
    path('home/',HomePage,name='home'),
    path('logout/',LogoutPage,name='logout'),
    path('video_feed/',video_feed, name='video_feed'),
    path('video/<int:pk>/',video_detail, name='video_detail'),
    path('channel/<int:pk>/',channel_detail, name='channel_detail'),
    path('video/<int:video_id>/like/', like_video, name='like_video'),
    path('add_video/',add_video, name='add_video'),
    path('video/<int:video_id>/add_comment/', add_comment, name='add_comment'),
    path('like_comment/<int:comment_id>/', like_comment, name='like_comment'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
