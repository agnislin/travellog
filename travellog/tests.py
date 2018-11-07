from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import User


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        pass
