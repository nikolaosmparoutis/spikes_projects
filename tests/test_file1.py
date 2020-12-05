import unittest
import sys
import os
# jenkins exposes the workspace directory through env. with this code can do import
# sys.path.append(os.environ['WORKSPACE'])
sys.path.append("/home/nikoscf/PycharmProjects/")
from file1 import func


class MyTestCase(unittest.TestCase):

    def test_file1_v1(self):
        in1 = 1
        in2 = 1
        actual = func(in1, in2)
        self.assertIs(actual, True, "Are equal")
        in1 = 1
        in2 = 2
        actual = func(in1, in2)
        self.assertIs(actual, False, "Are not equal")
        in1 = 0
        in2 = 2
        actual = func(in1, in2)
        self.assertEqual(actual, True, "a = 0")

        in1 = 'a'
        in2 = 'ab'
        actual = func(in1, in2)
        self.assertEqual(actual, False, "No same strings")


if __name__ == '__main__':
    unittest.main()



