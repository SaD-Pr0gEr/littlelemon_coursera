from unittest import TestCase

import requests
from django.urls import reverse


class TestMenuItemViews(TestCase):

    def test_view(self):
        response = requests.get(
            'http://127.0.0.1:8000' + reverse('restaurant_api:menu_items')
        )
        self.assertEqual(response.status_code, 200)
