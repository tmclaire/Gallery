# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
from .models import Location,Category,Image


from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.


# Create your views here.
def welcome(request):
    photos = Image.objects.all()

    return render(request, 'welcome.html')


def photos_of_day(request):
    
    date = dt.date.today()
    photos = Image.objects.all()
    return render(request, 'pictures/home.html', {"date": date,"photos":photos})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'pictures/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'pictures/search.html',{"message":message})
def location(request,location):
    images=Image.get_location_images(location=location)
    return render(request, 'pictures/location.html',{"photos": images})

def share(request,id):
    image=Image.share(id=id)
    return redirect(photos_of_day)
