import datetime

from django.db import models
from django.utils import timezone


# Class question has a question and a publication date
# This class Question is tested within the test_models.py
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


# Choice has two fields: the text of the choice and a vote tally. 
# Each Choice is associated with a Question
# This class Choice is tested within the test_models.py
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
