import unittest
import areas

class TestArea(unittest.TestCase):

    def test_triangle(self):
        self.assertEqual(areas.traingle(10, 5), 25)

    def test_rectangle(self):
        self.assertAlmostEqual(areas.rectangle(10, 5), 50)

    def test_square(self):
        self.assertAlmostEqual(areas.square(7), 49)

if __name__ == '__main__':
    unittest.main()