from django.shortcuts import render
from django.http import HttpResponse 
from .models import Tweet

# Create your views here.

def home_detail_view(request,tweet_id,*args,**kwargs):
    obj=Tweet.objects.get(id=tweet_id)
    return HttpResponse(f'<h1>Hello world! and hello {tweet_id}-{obj.content}</h1>')

def home_view(request,*args,**kwargs):
    return HttpResponse(f'<h1>HELLO <h1>')
