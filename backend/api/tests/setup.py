from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetup(APITestCase):
    fixtures = ['usersf']
    def setUp(self):        
        self.login_url = reverse(viewname="login")
        return super().setUp()

    def tearDown(self):
        return super().tearDown()