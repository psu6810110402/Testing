import unittest
from unittest.mock import patch
from coe_number.guess import guess_int, guess_float, is_in_range


class GuessIntStubTest(unittest.TestCase):
    
    @patch('coe_number.guess.random.randint', return_value=5)
    def test_guess_int_returns_stubbed_value(self, mock_randint):
        # Arrange
        start, stop = 1, 10
        expected = 5
        # Act
        result = guess_int(start, stop)
        # Assert
        self.assertEqual(result, expected)

    @patch('coe_number.guess.random.randint', return_value=5)
    def test_guess_int_calls_randint_with_correct_args(self, mock_randint):
        # Arrange
        start, stop = 1, 10
        # Act
        guess_int(start, stop)
        # Assert
        mock_randint.assert_called_once_with(start, stop)

    @patch('coe_number.guess.random.randint', return_value=1)
    def test_guess_int_stub_returns_boundary_min(self, mock_randint):
        # Arrange
        start, stop = 1, 100
        expected = 1
        # Act
        result = guess_int(start, stop)
        # Assert
        self.assertEqual(result, expected)

    @patch('coe_number.guess.random.randint', return_value=100)
    def test_guess_int_stub_returns_boundary_max(self, mock_randint):
        # Arrange
        start, stop = 1, 100
        expected = 100
        # Act
        result = guess_int(start, stop)
        # Assert
        self.assertEqual(result, expected)


class GuessFloatStubTest(unittest.TestCase):

    @patch('coe_number.guess.random.uniform', return_value=3.14)
    def test_guess_float_returns_stubbed_value(self, mock_uniform):
        # Arrange
        start, stop = 0.0, 10.0
        expected = 3.14
        # Act
        result = guess_float(start, stop)
        # Assert
        self.assertAlmostEqual(result, expected)

    @patch('coe_number.guess.random.uniform', return_value=0.0)
    def test_guess_float_stub_boundary_min(self, mock_uniform):
        # Arrange
        start, stop = 0.0, 1.0
        # Act
        result = guess_float(start, stop)
        # Assert
        self.assertAlmostEqual(result, 0.0)


class IsInRangeStubTest(unittest.TestCase):

    @patch('coe_number.guess.random.randint', return_value=5)
    def test_is_in_range_returns_true_when_in_range(self, mock_randint):
        # Arrange
        start, stop = 1, 10
        # Act
        result = is_in_range(None, start, stop)
        # Assert
        self.assertTrue(result)

    @patch('coe_number.guess.random.randint', return_value=1)
    def test_is_in_range_returns_true_at_lower_boundary(self, mock_randint):
        # Arrange
        start, stop = 1, 10
        # Act
        result = is_in_range(None, start, stop)
        # Assert
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
