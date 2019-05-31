from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# Create your views here.        AIzaSyCc3ufj6dlc6EYkQ41pRgvpFWHAHT5wHdA
#mysql> ALTER TABLE collabmates.search_searchdetail CONVERT TO CHARACTER SET utf8mb4;
#virtualenv -p python3 .
from django.shortcuts import render,reverse
from rest_framework import generics
from .models import SearchDetail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

DEVELOPER_KEY = 'AIzaSyCc3ufj6dlc6EYkQ41pRgvpFWHAHT5wHdA'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

#creating a class based view for easy pagination and filtering

class YoutubeSearchView(ListView):
    
    template_name = 'home.html'
    model = SearchDetail
    paginate_by = 10
    context_object_name = 'search_objects'
#this function creates and stores new objects in database and also gets the objects 
    def get_queryset(self):
        query = self.request.GET.get('q')
        Q = SearchDetail.objects.all().filter(query = query).order_by('-datetime')
        if not Q.exists() : 
            youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
            search_response = youtube.search().list(q=query,part='id,snippet',maxResults=20,order = 'date', publishedAfter='2010-01-01T00:00:00Z').execute()
            for item in search_response['items']:
                datetime= item['snippet']['publishedAt']
                description = item['snippet']['description']
                title =item['snippet']['title']
                thumbnail = item['snippet']['thumbnails']['default']['url']
                    #print(description)
                new = SearchDetail(title = title , description=description, thumbnail = thumbnail , datetime = datetime,query=query)
                new.save()
        return SearchDetail.objects.all().filter(query = query).order_by('-datetime')
#this functions gets the query from the url to our class based view
    def get_context_data(self, **kwargs):
        context = super(YoutubeSearchView, self).get_context_data(**kwargs)
        context['searchKey'] = self.request.GET.get('q')
        return context

