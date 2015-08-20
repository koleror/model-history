from django.db import models

class HistoryEntryManager(models.Manager):
    def create_entry(self, user, instance):
        # recursive function to handle unlimited level of fk
        def generate_diff(instance):
            # checks the db copy to compare updates
            original = instance._meta.model.objects.get(id=instance.id)
            data = {'model': instance.__module__ + instance.__class__.__name__, 'id': original.id, 'fields': {}}
            for field in instance._meta.fields:
                attr = getattr(instance, field.name)
                if isinstance(attr, models.Model):
                    sub = generate_diff(attr)
                    if sub['fields']:
                        data['fields'][field.name] = sub
                if getattr(original, field.name) != attr:
                    data['fields'][field.name] = getattr(instance, field.name)
            return data
        fields = generate_diff(instance)
        if user.is_superuser:
            status = self.model.ACTIVE
        else:
            status = self.model.DRAFT
        if fields['fields'] != {}:
            return self.model.objects.create(fields=fields, user=user, status=status)
        return None
