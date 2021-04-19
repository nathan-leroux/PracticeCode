import unittest

from Practice import *


class PracticeTest(unittest.TestCase):
    def test_practice_print(self):
        result = practice_print()
        self.assertEqual(result, 'this is a test')

    def test_practice_sum(self):
        input = [1,4,8,0]
        result = practice_sum(input)
        self.assertEqual(result, 13)


if __name__ =='__main__':
    unittest.main()