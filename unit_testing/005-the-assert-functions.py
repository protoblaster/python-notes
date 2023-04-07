import unittest

class TruthTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)

    def test_assert_false(self):
        self.assertFalse(False)

    def test_assert_true1(self):
        self.assertTrue(5 - 2) == 3

    def test_assert_false1(self):
        self.assertFalse(5 - 3) == 4

if __name__ == '__main__':
    unittest.main()