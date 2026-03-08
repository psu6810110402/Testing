import unittest
from coe_number.cat_and_mouse import cat_and_mouse

class CatAndMouseTest(unittest.TestCase):

    def test_cat_b_closer_returns_cat_b(self):
        # กรณีแมว B ใกล้กว่า
        a, b, c = 1, 2, 3
        res = cat_and_mouse(a, b, c)
        self.assertEqual(res, "Cat B")

    def test_equal_distance_returns_mouse_c(self):
        # กรณีระยะทางเท่ากัน หนูหนีไปได้
        a, b, c = 1, 3, 2
        res = cat_and_mouse(a, b, c)
        self.assertEqual(res, "Mouse C")

    def test_cat_b_closer_case2_returns_cat_b(self):
        a, b, c = 1, 5, 4
        res = cat_and_mouse(a, b, c)
        self.assertEqual(res, "Cat B")

    def test_cat_a_closer_returns_cat_a(self):
        a, b, c = 5, 1, 4
        res = cat_and_mouse(a, b, c)
        self.assertEqual(res, "Cat A")

    def test_cat_a_at_same_position_as_mouse(self):
        # แมว A อยู่ที่เดียวกับหนูเลย
        a, b, c = 5, 1, 5
        res = cat_and_mouse(a, b, c)
        self.assertEqual(res, "Cat A")

    def test_both_cats_at_same_position_as_mouse(self):
        # แมวทั้งสองตัวอยู่ที่เดียวกับหนู
        a, b, c = 3, 3, 3
        res = cat_and_mouse(a, b, c)
        self.assertEqual(res, "Mouse C")

    def test_return_type_is_string(self):
        # เช็คว่าส่งค่ากลับเป็น string ไหม
        res = cat_and_mouse(2, 5, 4)
        self.assertIsInstance(res, str)

    def test_result_is_one_of_valid_values(self):
        # เช็คว่าผลลัพธ์เป็นคำที่กำหนดไว้ไหม
        res = cat_and_mouse(10, 20, 15)
        self.assertIn(res, ["Cat A", "Cat B", "Mouse C"])

if __name__ == '__main__':
    unittest.main()
