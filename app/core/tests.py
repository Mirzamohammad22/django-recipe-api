from django.test import TestCase
from django.contrib.auth import get_user_model



class UserTest(TestCase):


    def test_user_created(self):

        email = 'abc@Gmail123.com'
        password = 'testabc123'


        user = get_user_model().objects.create(
            email = email,
            password = password
        )

        self.assertTrue(user.check_password(password))
        self.assertEqual(user.email, email.lower())

    def test_email_validation(self):

        email = None
        password = 'testabc12'

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create(
                        email = email,
                        password = password
                    )

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            email = 'test@mirza123.com',
            password = 'abc12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)




