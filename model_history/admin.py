from django.contrib import admin
from .models import HistoryEntry

class HistoryEntryAdmin(admin.ModelAdmin):
    model = HistoryEntry

admin.site.register(HistoryEntry, HistoryEntryAdmin)
