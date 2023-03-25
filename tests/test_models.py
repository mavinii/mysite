import unittest
from django.utils import timezone
import datetime
from django.test import TestCase

# Importing the models from polls folder
from polls.models import Question, Choice

"""
This class is testing the models.py Questions and Choice from polls folder
"""


class QuestionModelTests(TestCase):

    def test_str_method(self):
        question = Question(question_text="What's up?", pub_date=timezone.now())
        self.assertEqual(question.__str__(), "What's up?")

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=2)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class ChoiceModelTests(TestCase):

    def test_str_method(self):
        question = Question.objects.create(question_text="What's up?")
        choice = Choice.objects.create(question=question, choice_text="Not much")
        self.assertEqual(choice.__str__(), "Not much")

    def test_votes_default(self):
        question = Question.objects.create(question_text="What's up?")
        choice = Choice.objects.create(question=question, choice_text="Not much")
        self.assertEqual(choice.votes, 0)
