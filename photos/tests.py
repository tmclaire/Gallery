# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.

class ImageTestClass(TestCase):
      def setUp(self):
          self.category=Category(id=2134,category='photo')
          self.location=Location(id=1234,country='Rwanda',city='Kigali',place="Raddison blue")
          self.image=Image(image='@heroo',name='koko',description="koko koko koko okruuuuuu",location=self.location,category=self.category)

      def test_instance(self):
           self.assertTrue(isinstance(self.image, Image))
           self.assertTrue(isinstance(self.location,Location))
           self.assertTrue(isinstance(self.category,Category))

      def test_save_image(self):
          self.category.save()
          self.location.save()
          self.image.save_image()
          images = Image.objects.all()
          self.assertTrue(len(images) > 0)

      def test_delete_image(self):
         self.category.save()
         self.location.save()
         self.image.save_image()
         self.image.delete_image()
         images = Image.objects.all()
         self.assertTrue(len(images) == 0)

      def test_get_images_by_category(self):
          images=Image.get_category_images(category=self.category)
          imagess=Image.objects.filter(category=self.category)
          self.assertQuerysetEqual(images,imagess)
    
      def test_filter_by_location(self):
          images=Image.get_location_images(location=self.location.pk)
          imagess=Image.objects.filter(location=self.location)
          self.assertQuerysetEqual(images,imagess)

      def test_update_image(self):
        new_image=Image.name(1,'wow')
        self.assertTrue(self.image.name != new_image)

      def test_save_location(self):
         self.location.save_location()
         locations=Location.objects.all()
         self.assertTrue(len(locations)>0)

      def test_save_category(self):
         self.category.save_category()
         categories=Category.objects.all()
         self.assertTrue(len(categories)>0)
          
      def test_delete_location(self):
        
         self.location.delete_location()
         locations = Location.objects.all()
         self.assertTrue(len(locations) == 0)

      def test_delete_category(self):
        
         self.category.delete_category()
         categories= Category.objects.all()
         self.assertTrue(len(categories) == 0)

      def test_update_location(self):
          new_location=Location.update_all(1,'wow','wow','hi')
          self.assertTrue(self.location != new_location)

      def test_update_category(self):
          new_category=Category.update_name(1,'kiki')
          self.assertTrue(self.category.category != new_category)