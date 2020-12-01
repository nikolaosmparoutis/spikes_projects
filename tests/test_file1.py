import unittest
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


if __name__ == '__main__':
    unittest.main()
