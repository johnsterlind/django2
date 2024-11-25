import unittest

# A simple function to test
def add(a, b):
    return a + b

# Unit tests for the add function
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test case 1
        self.assertEqual(add(-1, 1), 0)  # Test case 2
        self.assertNotEqual(add(2, 2), 5)  # Test case 3

if __name__ == "__main__":
    unittest.main()