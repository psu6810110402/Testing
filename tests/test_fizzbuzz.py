import unittest
from coe_number.fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):

    def test_divisible_by_3_returns_fizz(self):
        val = 3
        expected = "Fizz"
        res = fizzbuzz(val)
        self.assertEqual(res, expected)

    def test_divisible_by_5_returns_buzz(self):
        val = 5
        expected = "Buzz"
        res = fizzbuzz(val)
        self.assertEqual(res, expected)

    def test_divisible_by_15_returns_fizzbuzz(self):
        val = 15
        expected = "FizzBuzz"
        res = fizzbuzz(val)
        self.assertEqual(res, expected)

    def test_not_divisible_returns_number_as_string(self):
        val = 7
        expected = "7"
        res = fizzbuzz(val)
        self.assertEqual(res, expected)

    def test_divisible_by_3_not_5_returns_fizz(self):
        val = 9
        expected = "Fizz"
        res = fizzbuzz(val)
        self.assertEqual(res, expected)

    def test_divisible_by_5_not_3_returns_buzz(self):
        val = 10
        expected = "Buzz"
        res = fizzbuzz(val)
        self.assertEqual(res, expected)

    def test_30_returns_fizzbuzz(self):
        val = 30
        expected = "FizzBuzz"
        res = fizzbuzz(val)
        self.assertEqual(res, expected)

    def test_1_returns_string_1(self):
        val = 1
        expected = "1"
        res = fizzbuzz(val)
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()
