from unittest import TestCase

from restaurant_api.models import MenuItem


class TestMenuItem(TestCase):

    def test_menu_item(self):
        item_title = 'Test'
        item = MenuItem.objects.create(
            title=item_title,
            price=10,
            inventory=1
        )
        self.assertEqual(item.title, item_title)
