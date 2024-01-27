from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TMFO = TopicModelForm()
    d = {'TMFO': TMFO}
    if request.method == 'POST':
        TMFC = TopicModelForm(request.POST)
        if TMFC.is_valid():
            TMFC.save()
            return HttpResponse('<center>TOpic inserted successfully</center>')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WMFO = WebpageModelForm()
    d = {'WMFO': WMFO}
    if request.method == 'POST':
        WMFC = WebpageModelForm(request.POST)
        if WMFC.is_valid():
            WMFC.save()
            return HttpResponse('<center>Webpage inserted</center>')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    AMFO = AccessModelForm()
    d = {'AMFO':AMFO}
    if request.method == 'POST':
        AMFC = AccessModelForm(request.POST)
        if AMFC.is_valid():
            AMFC.save()
            return HttpResponse('<center>AccessRecord Inserted</center>')
    return render(request,'insert_accessrecord.html',d)