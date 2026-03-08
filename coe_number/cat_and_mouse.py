def cat_and_mouse(x: int, y: int, z: int) -> str:
    """
    กำหนดตำแหน่งของแมว A (x), แมว B (y), และหนู C (z) บนเส้นตรง
    คืนค่าชื่อของแมวที่ถึงหนูก่อน หรือ 'Mouse C' ถ้าถึงพร้อมกัน
    Constraints: 1 <= x, y, z <= 100
    """
    dist_a = abs(x - z)
    dist_b = abs(y - z)

    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"
