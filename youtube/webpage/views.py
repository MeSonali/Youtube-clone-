from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from . models import Video,Channel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


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
        video = get_object_or_404(Video, id=pk)
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

def like_video(request, video_id):
    if request.method == "POST":
        video = get_object_or_404(Video, id=video_id)
        if request.user in video.likes.all():
            video.likes.remove(request.user)
        else:
            video.likes.add(request.user)
        return redirect('video_detail', pk=video_id)
    else:
        return HttpResponse(status=405)  
