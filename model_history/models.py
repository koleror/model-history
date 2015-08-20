from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from jsonfield import JSONField
from .managers import HistoryEntryManager

class ModelHistory(models.Model):
    class Meta:
        abstract = True

    def save_model(self, user):
        return HistoryEntry.objects.create_entry(user, self)


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

    class Meta:
        verbose_name_plural = "History entries"
