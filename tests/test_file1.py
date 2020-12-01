import unittest

class MyTestCase(unittest.TestCase):

    def test_file1(self):
        from file1 import func

        actual = func(1)
        self.assertIs(actual, False,"Are not str")
        actual = func("asd")
        self.assertIs(actual, True,"Are str")




if __name__ == '__main__':
    unittest.main()
