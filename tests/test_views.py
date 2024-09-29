from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        self.menu1 = Menu.objects.create(name='Pasta', price=12.99)
        self.menu2 = Menu.objects.create(name='Pizza', price=9.99)
        self.menu3 = Menu.objects.create(name='Salad', price=7.99)
        self.client = APIClient()

    def test_getall(self):
        # Make a GET request to the Menu endpoint
        response = self.client.get(reverse('menu-list'))  # assuming 'menu-list' is the name of your URL pattern

        # Retrieve all Menu objects and serialize them
        menus = Menu.objects.all()
        serialized_data = MenuItemSerializer(menus, many=True).data

        # Assert that the response data matches the serialized data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)
