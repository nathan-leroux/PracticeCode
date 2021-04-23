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
        self.assertEqual(stop_word_removal('this is a test', 'is a'), 'this test' )
        long_string =stop_word_removal('We know it is not just straightforward to jump from one car into another one, and only have one and half days of testing',
                                       'the and of is it if' )
        answer = 'We know not just straightforward to jump from one car into another one, only have one half days testing'
        self.assertEqual(long_string, answer)
        self.assertEqual(stop_word_removal('this the and this is is the the', 'the and this is'), '')

    def test_remove_punc(self):
        self.assertEqual(remove_punc('This, is. a! test$', ', . ! $'), 'This is a test')

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicate_words('aww baby aww awwbaby damn cmon'), 'aww awwbaby baby cmon damn')

    def test_clean_noise(self):
        self.assertEqual(cleaning_noise('http httpANDONE #blessed @Habib yee yeet&ampskeet bigsend\n'),
                         'yee yeet&skeet bigsend')

    def test_construct_ngram(self):
        expected_ngram = [['This', 'is', 'a'], ['is', 'a', 'long'], ['a', 'long', 'sentence']]
        result = construct_ngrams('This is a long sentence', 3)
        self.assertEqual(result, expected_ngram)
        self.assertEqual(construct_ngrams('smol test',3), [])

    def test_pos(self):
        self.assertEqual(pos('it\'s'), 'it')
        self.assertEqual(pos('gaps'), 'gap')
        self.assertEqual(pos('CMPS'), 'CMPS')
        self.assertEqual(pos('census'), 'census')
        self.assertEqual(pos('presses'), 'press')
        self.assertEqual(pos('cries'), 'cri')
        self.assertEqual(pos('tied'), 'tie')

    def test_word_ranking(self):
        fake_list = ['yes yes yes yes', 'no no no no yes', 'what what what que que ']
        self.assertEqual(word_ranking(fake_list, 3), [('yes', 5), ('no', 4), ('what', 3)])






if __name__ == '__main__':
    unittest.main()
