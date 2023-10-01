import unittest
from in_out import outer, square, pow

class TestInOut(unittest.TestCase):

    def test_outer_square(self):
        my_counter = outer(3, square)
        self.assertEqual(my_counter(), 9)
        self.assertEqual(my_counter(), 81)
        self.assertEqual(my_counter(), 6561)

    def test_outer_pow(self):
        another_counter = outer(1.5, pow)
        self.assertAlmostEqual(another_counter(), 1.8371173070873836)
        self.assertAlmostEqual(another_counter(), 3.056683336818703)
        self.assertAlmostEqual(another_counter(), 30.42684786675409)

if __name__ == "__main__":
    unittest.main()
