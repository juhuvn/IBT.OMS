from django import forms
from django.forms.models import inlineformset_factory
from models import *

class PublicationForm(forms.ModelForm):
    class Meta:
        model=Publication

Publication_propertyFomSet = inlineformset_factory(Publication, Publication_property, extra=5, can_delete=True)


class PropertyForm(forms.ModelForm):
    class Meta:
        model=Property

