# -*- coding: utf-8 -*-
import datetime as dt
from __future__ import unicode_literals

from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Gallery')


def photos_of_day(request):
    
    date = dt.date.today()
    photos = Image.objects.all()
    return render(request, 'pictures/home.html', {"date": date,"photos":photos})
