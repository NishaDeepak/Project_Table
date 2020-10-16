from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
from app.models import *
def display_topic(request):
    topics=Topic.objects.all()
    return render(request,'display_topic.html',context={'topics':topics})

def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='Skating')
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.filter(topic_name='Swimming').order_by('-name')
    #webpages=Webpage.objects.all()[: : -1]
    #webpages=Webpage.objects.exclude(topic_name='Skating')
    #webpages=Webpage.objects.filter(name__startswith='M')
    #webpages=Webpage.objects.filter(name__endswith='i')
    #webpages=Webpage.objects.filter(name__contains='s')
    #webpages=Webpage.objects.filter(Q(name__contains='n') & Q(name__startswith='a'))
    #webpages=Webpage.objects.filter(Q(name__contains='n'))
    return render(request,'display_webpage.html',context={'webpages':webpages})

def display_access(request):
    access=Access_Records.objects.all()
    #access=Access_Records.objects.filter(date__gt='2012-12-08')
    #access=Access_Records.objects.filter(date__gte='2012-12-08')
    #access=Access_Records.objects.filter(date__lte='2012-12-08')
    #access=Access_Records.objects.filter(date__month='12')
    #access=Access_Records.objects.filter(date__year='2012')
    #access=Access_Records.objects.filter(date__day='26')
    access=Access_Records.objects.filter(date__day__lt='18')
    return render(request,'display_access.html',context={'access':access})

def delete_webpage(request):
    #Webpage.objects.filter(name='Scott').delete()
    #Webpage.objects.all().delete()
    webpages=Webpage.objects.all()
    #return HttpResponse('One record has been deleted successfully')
    return render(request,'display_webpage.html',context={'webpages':webpages})

def update_webpage(request):
    #Webpage.objects.filter(topic_name='Swimming').update(name='Dhoni')
    #Webpage.objects.filter(name='Veronica').update(name='Monica',url='https://monica.com')
    t=Topic.objects.get_or_create(topic_name="Skating")[0]
    Webpage.objects.update_or_create(name='Lucy',defaults={'topic_name':t,url:'https://lucy.com'})
    webpages=Webpage.objects.all()
    return render(request,'display_webpage.html',context={'webpages':webpages})
