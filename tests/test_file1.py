import unittest
import sys
import os
# jenkins exposes the workspace directory through env.
sys.path.append(os.environ['WORKSPACE'])
import file1 as f


class MyTestCase(unittest.TestCase):

    def test_file1_v1(self):
        in1 = 1
        in2 = 1
        actual = f.func(in1, in2)
        self.assertIs(actual, True, "Are equal")
        in1 = 1
        in2 = 2
        actual = f.func(in1, in2)
        self.assertIs(actual, False, "Are not equal")


if __name__ == '__main__':
    unittest.main()
