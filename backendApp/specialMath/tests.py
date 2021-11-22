import unittest
from django.test import Client, RequestFactory, TestCase
import json

from .views import index

class TestSpecialMath(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_details(self):
        response = self.client.get('/specialmath/1/')
        data=json.loads(response.content)
        self.assertEqual(data['data']['output'], 1)

        response = self.client.get('/specialmath/0/')
        data=json.loads(response.content)
        self.assertEqual(data['data']['output'], 0)

        response = self.client.get('/specialmath/2/')
        data=json.loads(response.content)
        self.assertEqual(data['data']['output'], 3)

        response = self.client.get('/specialmath/3/')
        data=json.loads(response.content)
        self.assertEqual(data['data']['output'], 7)

        response = self.client.get('/specialmath/5/')
        data=json.loads(response.content)
        self.assertEqual(data['data']['output'], 26)

        response = self.client.get('/specialmath/7/')
        data=json.loads(response.content)
        self.assertEqual(data['data']['output'], 79)

        response = self.client.get('/specialmath/17/')
        data=json.loads(response.content)
        self.assertEqual(data['data']['output'], 10926)

        response = self.client.get('/specialmath/90/')
        data=json.loads(response.content)
        self.assertEqual(data['data']['output'], 19740274219868223074)

    def test_error(self):
        # incorrect inputs will return a 404 code
        response = self.client.get('/specialmath/a/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/specialmath/-3/')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/specialmath/3.4/')
        self.assertEqual(response.status_code, 404)