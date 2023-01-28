from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    tn=input('enter topic_name')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic is Inserted successfully')
    
def insert_webpage(request):
    tn=input('enter topic_name')
    name=input('enter name')
    url=input('enter url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=Sunny,url=sunny.com)[0]
    W.save()
    return HttpResponse('Webpage data is Inserted')