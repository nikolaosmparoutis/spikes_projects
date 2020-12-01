import unittest
import file1 as f

class MyTestCase(unittest.TestCase):
    def test_file1(self):
        actual = f.func(1)
        self.assertIs(actual, False,"Are not str")
        actual = f.func("asd")
        self.assertIs(actual, True,"Are str")




if __name__ == '__main__':
    unittest.main()
