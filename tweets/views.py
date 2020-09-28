from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home_view(request,tweet_id,*args,**kwargs):
    return HttpResponse(f'<h1>Hello world!and hello {tweet_id}</h1>')

def home_detail_view(request,id,*args,**kwargs):
    return HttpResponse(f'<h1>HELLO {id}<h1>')
