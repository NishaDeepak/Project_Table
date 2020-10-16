import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Table.settings')
import django
django.setup()
from app.models import *
import random
from faker import Faker
f1=Faker()
topics=['Skating','Swimming','Dieting','Cooking']

def Add_Topics():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def Add_Webpages(webpagename,url):
    topic=Add_Topics()
    w=Webpage.objects.get_or_create(topic_name=topic,name=webpagename,url=url)[0]
    w.save()
    return w

def Add_AccessRecords(webpagename,url,date):
    name=Add_Webpages(webpagename,url)
    a=Access_Records.objects.get_or_create(name=name,date=date)[0]
    a.save()

webpagename=f1.first_name()
url=f1.url()
date=f1.date()

def Add_date(n):
    for i in range(n):
        webpagename=f1.first_name()
        url=f1.url()
        date=f1.date()
        Add_AccessRecords(webpagename,url,date)

if __name__=='__main__':
    n=int(input('Enter number of rows to be inserted'))
    print('Population has been starting')
    Add_date(n)
    print('Population has been done successfully')