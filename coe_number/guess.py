import random

# ฟังก์ชันสุ่มเลขจำนวนเต็ม
def guess_int(start, stop):
    return random.randint(start, stop)

# ฟังก์ชันสุ่มเลขทศนิยม
def guess_float(start, stop):
    return random.uniform(start, stop)

# เช็คว่าเลขที่สุ่มได้อยู่ในช่วงไหม
def is_in_range(value, start, stop):
    res = guess_int(start, stop)
    if start <= res <= stop:
        return True
    else:
        return False
