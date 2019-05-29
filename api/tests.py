from django.test import TestCase
from api.models import Event
# Create your tests here.
class EventTest(TestCase):
    def test_str(self):
        event = Event.objects.create(name='MYname', is_vip=True)
        self.assertEqual(str(event), "{}:{}".format(event.name, event.is_vip))