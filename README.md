# COE Number - Python Unittest Project

โปรเจกต์ทดสอบการเขียน Unit Test ด้วย Python unittest สำหรับวิชาการเขียนโปรแกรม
ภาควิชาวิศวกรรมคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์

---

## โครงสร้างโปรเจกต์

```
project/
├── coe_number/
│   ├── __init__.py
│   ├── number_utils.py     # ตรวจสอบจำนวนเฉพาะ
│   ├── fizzbuzz.py         # FizzBuzz
│   ├── staircase.py        # บันได
│   ├── cat_and_mouse.py    # Cat and Mouse
│   └── guess.py            # สุ่มตัวเลข (ใช้สำหรับสาธิต Stub)
└── tests/
    ├── __init__.py
    ├── test_number_utils.py    # 8 test cases
    ├── test_fizzbuzz.py        # 8 test cases
    ├── test_staircase.py       # 8 test cases
    ├── test_cat_and_mouse.py   # 8 test cases
    └── test_guess_stub.py      # 6 test cases (Stub)
```

---

## วิธีรันทดสอบ

### รัน test ทั้งหมด

```bash
# Linux / macOS
python3 -m unittest -v

# Windows
python -m unittest -v
```

### รัน test เฉพาะไฟล์

```bash
python3 -m unittest -v tests/test_number_utils.py
python3 -m unittest -v tests/test_fizzbuzz.py
python3 -m unittest -v tests/test_staircase.py
python3 -m unittest -v tests/test_cat_and_mouse.py
python3 -m unittest -v tests/test_guess_stub.py
```

### รันพร้อม Code Coverage

```bash
pip install coverage nose2
nose2 -v --with-coverage --coverage coe_number
nose2 -v --with-coverage --coverage-report html
```

---

## รายละเอียด Test Cases

| ไฟล์                  | จำนวน Test | ครอบคลุม                             |
| --------------------- | ---------- | ------------------------------------ |
| test_number_utils.py  | 8          | True/False, จำนวนเฉพาะ, ตัวเลขประกอบ |
| test_fizzbuzz.py      | 8          | หาร 3, หาร 5, หาร 15, กรณีทั่วไป     |
| test_staircase.py     | 8          | รูปร่าง, ขอบเขต, error handling      |
| test_cat_and_mouse.py | 8          | Cat A, Cat B, Mouse C, type checking |
| test_guess_stub.py    | 6          | **Stub** ด้วย unittest.mock.patch    |

---

## Pattern ที่ใช้: Arrange-Act-Assert (AAA)

```python
def test_example(self):
    # Arrange - เตรียมข้อมูล
    x = 15
    expected = "FizzBuzz"

    # Act - เรียกใช้ฟังก์ชัน
    result = fizzbuzz(x)

    # Assert - ตรวจสอบผลลัพธ์
    self.assertEqual(result, expected)
```

---
