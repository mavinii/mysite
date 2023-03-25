from django.test import TestCase

# Importing the settings from mysite folder
from mysite.settings import SECRET_KEY

"""
In general, I should not include your SECRET_KEY in my test cases, 
as that would defeat the purpose of keeping it secret. 
Instead, I could create a separate .env file and set a unique SECRET_KEY value for that file. 
After that, I could add it to my .gitignore. 

But for purpose of learning, I am doing it as simply as possible.
"""


class SecretKeyTestCase(TestCase):
    def test_secret_key_is_set(self):
        self.assertNotEqual(SECRET_KEY, '')
