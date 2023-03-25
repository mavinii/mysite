from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import TestCase, LiveServerTestCase

"""
This is using a testing framework like Selenium, which allows me to 
simulate the user interactions with the website and test its functionality.
Docs: https://docs.djangoproject.com/en/4.1/topics/testing/tools/
"""


class LoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        # Load the login page
        self.browser.get(self.live_server_url + '/accounts/login/')

        # Fill in the login form
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('testuser')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('testpass')
        password_field.send_keys(Keys.RETURN)

        # Check that we have been redirected to the home page
        self.assertEqual(self.browser.current_url, self.live_server_url + '/')

        # Check that the user is now logged in
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('Logged in as testuser', navbar.text)
