import unittest
from main import *

class Tests(unittest.TestCase):
    def test_load_metrics(self):
        self.assertListEqual(['created_at',
              'tweet_ID',
              'valence_intensity',
              'anger_intensity',
              'fear_intensity',
              'sadness_intensity',
              'joy_intensity',
              'sentiment_category',
              'emotion_category'], list(load_metrics('input.txt')[0]))