from django.test import TestCase

# Create your tests here.

from .models import Event, User

class EventTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event.',
            date_time='2025-12-25 10:00:00',
            location='Test Location',
            organizer=self.user,
            capacity=100,
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
