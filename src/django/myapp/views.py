from django.shortcuts import render
from django.http import HttpResponse
from .models import SubscribedVideos
from datetime import datetime, timedelta


# Create your views here.
def index(request):

    #subscribed_videos = SubscribedVideos.objects.all()[:1000]
    subscribed_videos = SubscribedVideos.objects.filter(video_date__gte=datetime.now() - timedelta(days=14))

    genres = list({x.class_field for x in subscribed_videos})
    


    return(render(request,'main.html',{'subscribed_videos':subscribed_videos, 'genres': genres}))

