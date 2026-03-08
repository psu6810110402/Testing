import unittest
from coe_number.number_utils import is_prime_list

class PrimeListTest(unittest.TestCase):

    # ทดสอบกรณีที่เป็น True ทั้งหมด
    def test_give_1_2_3_is_prime(self):
        numbers = [1, 2, 3]
        res = is_prime_list(numbers)
        self.assertTrue(res)

    def test_give_single_prime_2(self):
        numbers = [2]
        res = is_prime_list(numbers)
        self.assertTrue(res)

    def test_give_primes_5_7_11_13(self):
        numbers = [5, 7, 11, 13]
        res = is_prime_list(numbers)
        self.assertTrue(res)

    def test_give_single_prime_17(self):
        numbers = [17]
        res = is_prime_list(numbers)
        self.assertTrue(res)

    # ทดสอบกรณีที่มีเลขไม่ใช่จำนวนเฉพาะ
    def test_give_list_with_composite_4(self):
        numbers = [2, 3, 4]
        res = is_prime_list(numbers)
        self.assertFalse(res)

    def test_give_list_with_composite_9(self):
        numbers = [3, 9]
        res = is_prime_list(numbers)
        self.assertFalse(res)

    def test_give_single_composite_6(self):
        numbers = [6]
        res = is_prime_list(numbers)
        self.assertFalse(res)

    def test_give_large_composite_100(self):
        numbers = [100]
        res = is_prime_list(numbers)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
