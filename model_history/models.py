from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from jsonfield import JSONField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from .managers import HistoryEntryManager



class HistoryEntry(models.Model):
    objects = HistoryEntryManager()
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DRAFT = 'draft'
    STATUSES = (
        (ACTIVE, _('Active')),
        (INACTIVE, _('Inactive')),
        (DRAFT, _('Draft')),
    )
    status = models.CharField(choices=STATUSES, default=DRAFT, max_length=8)
    fields = JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='history_entries')
    content_type = models.ForeignKey(ContentType, default=None, null=False)
    object_id = models.PositiveIntegerField(default=None, null=False)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = "History entries"


class ModelHistory(models.Model):
    history_entries = generic.GenericRelation(HistoryEntry)
    class Meta:
        abstract = True

    def save_model(self, user):
        return HistoryEntry.objects.create_entry(user, self)
