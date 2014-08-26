# -*- coding: utf-8 -*-
__author__ = 'Ga Go'
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from publication.forms import *
from publication.models import *

def index(request):
    publications = Publication.objects.order_by('title')
    context = {'publications': publications}
    return render(request, 'publication/index.html', context)

# ___DETAIL CHƯA ĐƯỢC___
def detail(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    property = publication.publication_property_set.all()
    context = {'publication': publication, 'property':property}
    return render(request, 'publication/detail.html', context)

def add_property(request):
    form = PropertyForm()
    if request.method =='POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save()
            return HttpResponse("Added Successfully")

    return render(request, "publication/add_property.html", {
        'form': form,
        'action': "Add property"
    })

def add(request):
    form = PublicationForm()
    publication_property_formset = Publication_propertyFomSet(instance=Publication())

    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save()
            publication_property_formset = Publication_propertyFomSet(request.POST, instance=publication)
            if publication_property_formset.is_valid():
                publication_property_formset.save()
                return HttpResponse("Added Successfully")

    return render(request, "publication/add.html", {
        'form': form,
        'publication_property_formset': publication_property_formset,
        'action': "Add publication"
    })

def update(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    form = PublicationForm(instance=publication)
    pub_pro_formset = Publication_propertyFomSet(instance=publication)

    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            publication = form.save(commit=False)
            pub_pro_formset = Publication_propertyFomSet(request.POST, instance=publication)
            if pub_pro_formset.is_valid():
                publication.save()
                pub_pro_formset.save()
                return HttpResponse("Updated Successfully!")

    return render(request, "publication/add.html", {
        'form':form,
        'pub_pro_formset': pub_pro_formset,
        'action': "Update Publication"})