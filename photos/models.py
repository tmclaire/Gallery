# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Location(models.Model):
     country=models.CharField(max_length=50)
     city=models.CharField(max_length=50)
     place=models.CharField(max_length=50,default='unkown',null=True)
     def __str__(self):
        return self.country
     def save_location(self):
         self.save()
     def delete_location(self):
      self.delete()

     @classmethod
     def update_all(cls,id,new,newer,newest):
      location=Location.objects.filter(id=id)
      location.update(country=new,city=newer,place=newest)
      return location




class Category(models.Model):
     category=models.CharField(max_length=50)
     def __str__(self):
        return self.category

     def save_category(self):
         self.save()

     def delete_category(self):
      self.delete()

     @classmethod
     def update_name(cls,id,new):
      category=Category.objects.filter(id=id)
      category.update(category=new)
      return category

class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name= models.CharField(max_length =30)
    description=models.TextField()
    location=models.ForeignKey(Location,null=True)
    category=models.ForeignKey(Category, null=True)
    url=models.TextField(max_length=500, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    def save_image(self):
         self.save()
    def delete_image(self):
      self.delete()
    
    @classmethod
    def get_image(cls,id):
    
      image=Image.objects.filter(id=id)
      return image

    @classmethod
    def get_category_images(cls,cat):
      categori=Category.objects.filter(category=cat).first()
      images=Image.objects.filter(category=categori)
      return images

    @classmethod
    def get_location_images(cls,loc):
      locati=Location.objects.filter(pk=loc)
      images=Image.objects.filter(location=locati)
      return images

    @classmethod
    def search_by_category(cls,search_term):
                category = Category.objects.filter(category__icontains=search_term).first()
                image = cls.objects.filter(category=category)
                return image



      



    

