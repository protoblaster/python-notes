import unittest
import triangle_area

class TestArea(unittest.TestCase):

#    def test_triangle(self):
#        result = triangle_area.triangle(10, 5)
#        self.assertEqual(result, 25)

    def runTest(self):
        result = triangle_area.triangle(10, 5)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()

# when using unittest framework we must give a test case
# a name beginning with test_