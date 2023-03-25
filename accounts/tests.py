from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .views import SignUpView


# This first class, SignUpTests, contains tests that make sure the SignUpView returns a 200 status code
class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func.view_class, SignUpView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)

    def test_form_inputs(self):
        """
        The view must contain five inputs: csrf, username, email,
        password1, password2
        """
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="submit"', 1)


# This second class, SuccessfulSignUpTests, contains tests that check if a valid form submission
# redirects the user to the home page, creates a new user, and authenticates the user.
class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@example.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        """
        A valid form submission should redirect the user to the home page
        """
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        """
        Create a new request to an arbitrary page.
        The resulting response should now have a 'user' to its context,
        after a successful sign up.
        """
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


# The third class, InvalidSignUpTests, contains tests that check if an invalid form
# submission returns to the same page and contains form errors
class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        # Submit an empty dictionary, this should raise a form validation error.
        self.response = self.client.post(url, {})

    def test_signup_status_code(self):
        """
        An invalid form submission should return to the same page
        """
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)


