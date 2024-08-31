from django.db import models
from django.contrib.auth.models import User

class Channel(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='channel_logo/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnail/', default=None)
    views = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)
    # likes = models.IntegerField(default=0, blank=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='videos')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')  
    likes = models.ManyToManyField(User, related_name='liked_videos', blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    

    



    
    # likes = models.ManyToManyField(User, related_name='liked_videos', blank=True)
    # channel = models.ForeignKey('Channel', on_delete=models.CASCADE)

