# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type = models.CharField(u'Loại', max_length=96)

    def __unicode__(self):
        return self.type

class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    #type_id = models.ForeignKey(Type)
    name = models.CharField(u'Thuộc tính', max_length=256)

    def __unicode__(self): # Python 3: def __str__(self):
        return self.name

class Lab(models.Model):
    #lab_ID = models.CharField(max_length=64)
    name = models.CharField(u'Phòng', max_length=512)
    def __unicode__(self): # Python 3: def __str__(self):
        return self.name

class Author(models.Model):
    #author_ID = models.CharField(max_length=64)
    lab = models.ForeignKey(Lab)
    name = models.CharField(u'Tên', max_length=512)
    def __unicode__(self): # Python 3: def __str__(self):
        return self.name

class Publication(models.Model):
    #publication_id = models.AutoField(primary_key=True)
    title = models.CharField(u'Tên', max_length=1024)
    type = models.ForeignKey(Type, verbose_name=u'Loại')
    author=models.ManyToManyField(Author)


    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Publication._meta.fields]

    def __unicode__(self): # Python 3: def __str__(self):
        return self.title

class Publication_property (models.Model):
    publication_property_id = models.AutoField(primary_key=True)
    publication = models.ForeignKey(Publication)
    name = models.ForeignKey(Property)
    value = models.CharField(max_length=1024)

    def __unicode__(self): # Python 3: def __str__(self):
        return self.value
