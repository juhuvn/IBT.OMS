from django.contrib import admin
from django.db.models import get_models, get_app
from publication.models import *

class PublicationInline(admin.TabularInline):
    model = Publication
    extra = 1

class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationInline]

admin.site.register(Lab)
admin.site.register(Author)
admin.site.register(Publication)
admin.site.register(Type)
admin.site.register(Property)
admin.site.register(Publication_property)