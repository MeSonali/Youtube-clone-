from django.shortcuts import render
from django.http import HttpResponse
from . models import Video,Channel
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.method == "GET":
        # return render(request, 'video_feed.html')
        pass
    if request.method == 'POST':
        pass


def video_feed(request):
    if request.method == "GET":
        videos = Video.objects.all()
        context ={
            'videos': videos
            }
       
        return render(request, 'video_feed.html',context )
    if request.method == 'POST':
        pass

def video_detail(request, pk):
    if request.method == "GET":
        video = get_object_or_404(Video, pk=pk)
        context = {'video': video}
        return render(request, 'video_detail.html', context)
    if request.method == "POST":
        pass


def channel_detail(request, pk):
    if request.method == "GET":
        channel = get_object_or_404(Channel, pk=pk)
        videos = channel.videos.all()  
        context =  {'channel': channel, 'videos': videos}
        return render(request, 'channel_detail.html',context)
    if request.method == "POST":
        pass
