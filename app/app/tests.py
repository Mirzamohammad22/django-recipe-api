from django.test import TestCase

from app.cal import add

class CalTests(TestCase):

    def test_add_number(self):
        """ Test that two numbers are added"""
        self.assertEqual(add(10,20),30)