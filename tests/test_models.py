from django.test import TestCase
from django.contrib.auth import get_user_model



class UserTest(TestCase):


    def user_created(self):

        email = 'abc@gmail123.com'
        password = 'testabc123'


        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertNotEqual(user.email,email)
        self.assertTrue(user.check_password(password))
