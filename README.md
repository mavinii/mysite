# Continuous Assessment 1 - November 2022
This project was created based on [Django Documentation](https://docs.djangoproject.com/en/4.1/).

- Back-End Web Development - BSC30922 & BTM0922 - Semester 1 & 2.
- Student n: `22931`
- Student name: `Marcos Oliveira`
- Tutor: [Geoff-Wright](https://github.com/Geoff-Wright). 

### Writing your first Django app, part 1:
[Django Documentation, part 1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
- Creating a project
- The development server
- Creating the Polls app
- Write your first view

For running the server type on `terminal`:
> py manage.py runserver

> http://127.0.0.1:8000/

> http://127.0.0.1:8000/polls/

### Writing your first Django app, part 2:
[Django Documentation, part 2](https://docs.djangoproject.com/en/4.1/intro/tutorial02/)
- Database setup
- Creating models.
- Activating models.
- Playing with the API.
- Creating an admin user.
#### Admin details:
> http://127.0.0.1:8000/admin/ 
- Username: `pgmar`
- Email: `example@admin.com`
- Password: `123456`

### Writing your first Django app, part 3:
[Django Documentation, part 3](https://docs.djangoproject.com/en/4.1/intro/tutorial03/)
- Writing more views
- Raising a 404 error
- Use the template system
- Removing hardcoded URLs in templates
- Namespacing URL names

### Writing your first Django app, part 4:
[Django Documentation, part 4](https://docs.djangoproject.com/en/4.1/intro/tutorial04/)
- Write a minimal form
- Amend URLconf
- Amend views (generic views)

### Writing your first Django app, part 6:
[Django Documentation, part 6](https://docs.djangoproject.com/en/4.1/intro/tutorial06/)
- Customize your app’s look and feel
- Adding a background-image

# Continuous Assessment 2 - December 2022
All security issues necessary for this project are fixed.

### Login and Logout:
[Login and Logout Documentation](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
- The Django auth app
- Login Page
- User Details:
    - Username: `user`
    - Email: `user@user.com`
    - Password: `123456`
- Create a homepage
- Logout link
- Conclusion

## Reset Password:
[Django Password Reset Tutorial](https://learndjango.com/tutorials/django-password-reset-tutorial)
- Django lets us store emails either in the console or as a file.
- http://127.0.0.1:8000/accounts/password_reset/

## Customizations:
- Using [Bootstrap](https://getbootstrap.com/).

# Continuous Assessment 3 - Django Test and Security
For my CA3 project, I created a test folder to store all my tests. Within that folder, the files I have created are: `test_models.py`, `test_urls.py`, `test_settings.py`, `test_login.py` and `test_signup`.

- test_models.py:

		- I wrote test cases to verify the behavior of the Question and Choice models in the polls app. 

- test_urls.py:

		- I wrote test cases to verify that the URL patterns in the polls app are resolving to the expected views.These tests helped me to ensure that the routing in the app is set up correctly and that URLs are resolving to the appropriate views.


- test_settings.py:

		- basically, it tests to see if the secrete_key is valid or not, I should not include your SECRET_KEY, as that would defeat the purpose of keeping it secret. Instead, I could create a separate .env file and set a unique SECRET_KEY value for that file. After that, I could add it to my .gitignore. But for purpose of learning, I am doing it as simply as possible.


- test_login.py and test_signup.py:

		- This is using a testing framework like Selenium, which allows me to simulate the user interactions with the website and test its functionality.
		

- 'django.middleware.security.SecurityMiddleware':

		- The middleware provides security features for your application, such as setting HTTP headers to protect 	against common attacks like cross-site scripting (XSS), cross-site request forgery (CSRF), and clickjacking.


These tests provide a safety net for my CA3 project, helping me catch bugs and regressions as I make changes to the codebase.



### This project was created based on Django Documentation:
- [Django Documentation, part 5](https://docs.djangoproject.com/en/4.1/intro/tutorial05/)
- [Unittest Python Docs](https://docs.python.org/3/library/unittest.html)
- [URL dispatcher](https://docs.djangoproject.com/en/3.2/topics/http/urls/)
- [Writing views](https://docs.djangoproject.com/en/3.2/topics/http/views/)
- [Django Testing tools](https://docs.djangoproject.com/en/4.1/topics/testing/tools/)

## Pages:
![main page](/polls/static/pages/1.png)
![admin page](/polls/static/pages/2.png)
![sign-in page](/polls/static/pages/3.png)
![welcome page](/polls/static/pages/4.png)
![all question page](/polls/static/pages/5.png)
![question page](/polls/static/pages/6.png)
![total votes page](/polls/static/pages/7.png)