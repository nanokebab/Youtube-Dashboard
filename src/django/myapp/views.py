from django.shortcuts import render
from django.http import HttpResponse
from .models import SubscribedVideos
from datetime import datetime, timedelta


# Create your views here.
def index(request):

    # Get the selected producers from the GET request (if any)
    selected_channel_names = request.GET.getlist('channel_name')

    #subscribed_videos = SubscribedVideos.objects.all()[:1000]
    subscribed_videos = SubscribedVideos.objects.filter(video_date__gte=datetime.now() - timedelta(days=14)).exclude(channel_name__in=selected_channel_names)

    genre_map_list = SubscribedVideos.objects.order_by().values_list('class_field','channel_name').distinct()
    genre_map_dict = {}
    for x, y in genre_map_list:
        genre_map_dict.setdefault(x, []).append(y)


    genres = list({x.class_field for x in subscribed_videos})
    
    # Get the list of all producers
    all_channel_names = SubscribedVideos.objects.values_list('channel_name', flat=True).distinct()

    context = {
        'subscribed_videos':subscribed_videos, 
        'genres': genres,
        'genre_map_dict': genre_map_dict,
        'all_channel_names': all_channel_names,
        'selected_channel_names': selected_channel_names
        }

    return(render(request,'main.html',context))