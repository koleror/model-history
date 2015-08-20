from django.contrib import admin
from .models import Sample

class SampleAdmin(admin.ModelAdmin):
    model = Sample

admin.site.register(Sample, SampleAdmin)
