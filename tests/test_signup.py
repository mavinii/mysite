from django.test import Client, TestCase

"""
This is using a testing framework like Selenium, which allows you to 
simulate user interactions with the website and test its functionality.
Docs: https://docs.djangoproject.com/en/4.1/topics/testing/tools/
"""


class SignUpPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_page(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
