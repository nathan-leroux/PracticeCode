import unittest
from Assignment import *


class Tests(unittest.TestCase):
    def test_caps(self):
        self.assertEqual(proper_capitalization('THIS? is, A. DuMb Sentence'), 'this? is, a. dumb sentence')

    def test_tokenization(self):
        self.assertEqual(tokenization('this is a test'), ['this', 'is', 'a', 'test'])

    def test_trim_word(self):
        self.assertEqual(trim_word('sentence', ['t', 'zen', 'ce']), 'senten')

    def test_stop_word(self):
        self.assertEqual(stop_word_removal('this, is. a test', 'is a'), 'this, test' )

    def test_remove_punc(self):
        self.assertEqual(remove_punc('This, is. a! test$', ',.!$'), 'This is a test')

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicate_words('aww baby aww awwbaby damn cmon'), 'aww awwbaby baby cmon damn')

    def test_clean_noise(self):
        self.assertEqual(cleaning_noise('http httpANDONE #blessed @Habib yee yeet&ampskeet big\nsend \n'),
                         'yee yeet&skeet bigsend')

    def test_construct_ngram(self):
        expected_ngram = [['This', 'is', 'a'], ['is', 'a', 'long'], ['a', 'long', 'sentence']]
        result = construct_ngrams('This is a long sentence', 3)
        self.assertEqual(result, expected_ngram)
        self.assertEqual('smol test', [])






if __name__ == '__main__':
    unittest.main()
