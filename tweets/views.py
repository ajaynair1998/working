import random
from django.shortcuts import render
from django.http import HttpResponse ,Http404,JsonResponse
from .models import Tweet
from .forms import TweetForm

# Create your views here.

# def home_detail_view(request,tweet_id,*args,**kwargs):
#     '''
#     rest api view 
#     Consume by js or swift or java or ios or android
#     return json data
#     '''
#     try:
#         obj=Tweet.objects.get(id=tweet_id)
#     except:
#         raise Http404
#     return HttpResponse(f'<h1>Hello world! and hello {tweet_id}-{obj.content}</h1>')
def tweet_create_view(request,*args,**kwargs):
    form=TweetForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        form=TweetForm()
    return render(request,'components/form.html',context={'form':form})


def tweet_list_view(request,*args,**kwargs):
    '''rest api view'''
    qs=Tweet.objects.all()
    tweets_list=[{'id':x.id,'content':x.content,'likes':random.randint(0,500)} for x in qs]
    data={'isuser':False,'response':tweets_list}
    return JsonResponse(data)

def home_detail_view(request,tweet_id,*args,**kwargs):
    data={
        'id':tweet_id
        #image_path':obj.image.url
    }
    status=200
    try:
        obj=Tweet.objects.get(id=tweet_id)
        data['content']=obj.content
    except:
        data['message']='Not Found'
        status=404

    

    return JsonResponse(data,status=status)

def home_view(request,*args,**kwargs):
    return render(request,'pages/home.html',context={},status=200)
    # return HttpResponse(f'<h1>HELLO <h1>')
