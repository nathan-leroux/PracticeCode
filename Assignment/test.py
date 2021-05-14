import unittest
from A2_22476883 import *


class Tests(unittest.TestCase):
    def test_caps(self):
        self.assertEqual(proper_capitalization('THIS? is, A. DuMb Sentence'), 'this? is, a. dumb sentence')

    def test_tokenization(self):
        self.assertEqual(tokenization('this is a test'), ['this', 'is', 'a', 'test'])

    def test_trim_word(self):
        self.assertEqual(trim_word('sentence', ['t', 'zen', 'ce']), 'senten')

    def test_stop_word(self):
        self.assertEqual(stop_word_removal('this is a test', 'is a'), 'this test' )
        long_string =stop_word_removal('We know it is not just straightforward to jump from one car into another one, and only have one and half days of testing',
                                       'the and of is it if' )
        answer = 'We know not just straightforward to jump from one car into another one, only have one half days testing'
        self.assertEqual(long_string, answer)
        self.assertEqual(stop_word_removal('this the and this is is the the', 'the and this is'), '')

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicate_words('aww baby aww awwbaby damn cmon'), 'aww awwbaby baby cmon damn')

    def test_construct_ngram(self):
        expected_ngram = [['This', 'is', 'a'], ['is', 'a', 'long'], ['a', 'long', 'sentence']]
        result = construct_ngrams('This is a long sentence', 3)
        self.assertEqual(result, expected_ngram)
        self.assertEqual(construct_ngrams('smol test',3), [])
        self.assertEqual(construct_ngrams('this is another long sentence for testing', 5), [['this', 'is', 'another', 'long', 'sentence', 'for'], ['is', 'another', 'long', 'sentence', 'for', 'testing']])

    def test_pos(self):
        self.assertEqual(pos('it\'s'), 'it')
        self.assertEqual(pos('gaps'), 'gap')
        self.assertEqual(pos('CMPS'), 'CMPS')
        self.assertEqual(pos('census'), 'census')
        self.assertEqual(pos('presses'), 'press')
        self.assertEqual(pos('cries'), 'cri')
        self.assertEqual(pos('tied'), 'tie')






if __name__ == '__main__':
    unittest.main()
