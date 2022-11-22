from django.contrib import admin

# This is the admin file in the polls app
from .models import Question

admin.site.register(Question)