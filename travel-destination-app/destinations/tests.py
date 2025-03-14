from django.test import TestCase
from .models import Destination

class DestinationModelTest(TestCase):

    def setUp(self):
        Destination.objects.create(name="Paris", description="The city of lights", country="France")
        Destination.objects.create(name="Tokyo", description="The bustling capital of Japan", country="Japan")

    def test_destination_creation(self):
        paris = Destination.objects.get(name="Paris")
        tokyo = Destination.objects.get(name="Tokyo")
        self.assertEqual(paris.description, "The city of lights")
        self.assertEqual(tokyo.country, "Japan")

    def test_destination_str(self):
        destination = Destination(name="New York")
        self.assertEqual(str(destination), destination.name)