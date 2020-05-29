from django.test import TestCase, SimpleTestCase


# Create your tests here.
from django.urls import reverse


class SimpleTests(SimpleTestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code,200)


    def test_aboutus_page_works(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code,200)