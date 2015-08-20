from django import forms
from model_history.forms import ModelHistoryForm
from .models import Sample

class SampleForm(ModelHistoryForm):
    class Meta:
        model = Sample
        fields = ['string', 'boolean', 'link']
