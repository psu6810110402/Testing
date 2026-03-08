def is_prime_list(numbers):
    # วนลูปเช็คตัวเลขทุกตัวในลิสต์
    for num in numbers:
        # ถ้าเป็น 1 ให้ข้ามไป (โจทย์บอกให้เป็น True)
        if num == 1:
            continue
        # เช็คว่าเป็นจำนวนเฉพาะไหม
        for n in range(2, num):
            if num % n == 0:
                return False # ถ้าหารลงตัว แสดงว่าไม่ใช่จำนวนเฉพาะ
    return True # ถ้าผ่านหมดแสดงว่าเป็นจำนวนเฉพาะทุกตัว
