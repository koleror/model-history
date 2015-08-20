from django.db import models
from model_history.models import ModelHistory


class SampleFK(models.Model):
    data = models.CharField(max_length=100, default=None, null=True, blank=True)


class Sample(ModelHistory):
    string = models.CharField(max_length=100, default=None, null=True, blank=True)
    boolean = models.BooleanField(default=True)
    link = models.ForeignKey(SampleFK, null=True, default=None, blank=True)

    def get_absolute_url(self):
        return '/samples/%d' % self.id
