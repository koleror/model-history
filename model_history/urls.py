"""
model_history URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'model_history.views.home_page', name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^samples/$', 'sample.views.list_samples', name="list_samples"),
    url(r'^samples/([0-9]+)/$', 'sample.views.one_sample'),
]
