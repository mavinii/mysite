import unittest
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Importing the urls from polls folder
from polls.urls import views

"""
This class is testing the urls.py views from polls folder
"""


class PollsUrlsTestCase(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('polls:index')
        self.assertEqual(resolve(url).func.view_class, views.IndexView)

    def test_detail_url_resolves(self):
        url = reverse('polls:detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.DetailView)

    def test_results_url_resolves(self):
        url = reverse('polls:results', args=[1])
        self.assertEqual(resolve(url).func.view_class, views.ResultsView)

    def test_vote_url_resolves(self):
        url = reverse('polls:vote', args=[1])
        self.assertEqual(resolve(url).func, views.vote)
