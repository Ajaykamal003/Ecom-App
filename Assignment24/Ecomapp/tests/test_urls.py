from django.test import TestCase
from django.urls import resolve, reverse
from Ecomapp.views import home

class TestURL(TestCase):
    def testurlhome(self):
        url = reverse('product_by_category', args=['demo-slug'])
        print("Resolve: ", resolve(url))
        self.assertEqual(resolve(url).func, home)
