import unittest
from coe_number.staircase import staircase


class StaircaseTest(unittest.TestCase):

    def test_give_2_with_hash_should_return_correct_shape(self):
        # Arrange
        n = 2
        pattern = '#'
        expected = " #\n##"
        # Act
        result = staircase(n, pattern)
        # Assert
        self.assertEqual(result, expected, f"Should be:\n{expected}")

    def test_give_1_returns_single_character(self):
        # Arrange
        n = 1
        pattern = '#'
        expected = "#"
        # Act
        result = staircase(n, pattern)
        # Assert
        self.assertEqual(result, expected)

    def test_give_4_with_hash_correct_shape(self):
        # Arrange
        n = 4
        pattern = '#'
        expected = "   #\n  ##\n ###\n####"
        # Act
        result = staircase(n, pattern)
        # Assert
        self.assertEqual(result, expected)

    def test_give_3_with_star_pattern(self):
        # Arrange
        n = 3
        pattern = '*'
        expected = "  *\n **\n***"
        # Act
        result = staircase(n, pattern)
        # Assert
        self.assertEqual(result, expected)

    def test_last_row_has_no_leading_space(self):
        # Arrange
        n = 5
        pattern = '#'
        # Act
        result = staircase(n, pattern)
        last_row = result.split('\n')[-1]
        # Assert
        self.assertEqual(last_row, '#####', "แถวสุดท้ายต้องไม่มี space นำหน้า")

    def test_first_row_has_n_minus_1_spaces(self):
        # Arrange
        n = 5
        pattern = '#'
        # Act
        result = staircase(n, pattern)
        first_row = result.split('\n')[0]
        # Assert
        self.assertEqual(first_row, '    #', "แถวแรกต้องมี space นำหน้า n-1 ช่อง")

    def test_invalid_n_zero_raises_value_error(self):
        # Arrange / Act / Assert
        with self.assertRaises(ValueError):
            staircase(0)

    def test_invalid_n_over_30_raises_value_error(self):
        # Arrange / Act / Assert
        with self.assertRaises(ValueError):
            staircase(31)


if __name__ == '__main__':
    unittest.main()
