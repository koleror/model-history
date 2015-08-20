from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from .models import ModelHistory, HistoryEntry


# Tests models to help test ModelHistory model inheritance
class TestModel2(models.Model):
    string = models.CharField(max_length=100, default=None, null=True, blank=True)


class TestModel(ModelHistory):
    string = models.CharField(max_length=100, default=None, null=True, blank=True)
    boolean = models.BooleanField(default=True)
    link = models.ForeignKey(TestModel2, null=True, default=None)


class ModelHistoryTest(TestCase):
    def setUp(self):
        super(ModelHistoryTest, self).setUp()
        self.sample = TestModel.objects.create(string='X', boolean=False,
                                               link=TestModel2.objects.create(string='test'))
        self.admin = User.objects.create(is_staff=True, is_superuser=True, username='admin')
        self.user = User.objects.create(username='user')

    def test_created(self):
        self.assertEqual(HistoryEntry.objects.count(), 0)
        self.sample.boolean = True
        self.sample.save_model(self.user)
        self.assertEqual(HistoryEntry.objects.count(), 1)

    def test_status_regular_user(self):
        self.sample.boolean = True
        self.sample.save_model(self.user)
        entry = HistoryEntry.objects.get()
        self.assertEqual(entry.status, entry.DRAFT)

    def test_status_super_user(self):
        self.sample.boolean = True
        self.sample.save_model(self.admin)
        self.assertEqual(HistoryEntry.objects.get().status, HistoryEntry.ACTIVE)

    def test_updated_fields_populated(self):
        self.sample.boolean = True
        self.sample.save_model(self.admin)
        self.assertEqual(HistoryEntry.objects.get().fields['fields'], {'boolean': True})

    def test_no_fields_updated_case(self):
        self.sample.save_model(self.admin)
        self.assertEqual(HistoryEntry.objects.count(), 0)

    def test_set_fk_model_none(self):
        self.sample.link = None
        self.sample.save_model(self.admin)
        self.assertEqual(HistoryEntry.objects.count(), 1)
        self.assertEqual(HistoryEntry.objects.get().fields['fields'], {'link': None})

    def test_update_fk_attr(self):
        self.sample.link.string = 'yes'
        self.sample.save_model(self.admin)
        self.assertEqual(HistoryEntry.objects.count(), 1)
        entry = HistoryEntry.objects.get()
        self.assertEqual(entry.fields['fields'].keys(), ['link'])
        self.assertEqual(entry.fields['fields']['link']['model'], 'model_history.testsTestModel2')
        self.assertEqual(entry.fields['fields']['link']['fields'].keys(), ['string'])
        self.assertEqual(entry.fields['fields']['link']['fields']['string'], 'yes')
