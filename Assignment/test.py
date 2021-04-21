import unittest
from Assignment import *


class Tests(unittest.TestCase):
    def test_caps(self):
        self.assertEqual(proper_capitalization('THIS? is, A. DuMb Sentence'), 'this? is, a. dumb sentence')

if __name__ == '__main__':
    unittest.main()
