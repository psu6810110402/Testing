def staircase(n, pattern='#'):
    # เช็คเงื่อนไขว่า n อยู่ในช่วง 1-30 ไหม
    if n <= 0 or n > 30:
        raise ValueError("n must be between 1 and 30")

    result = []
    for i in range(1, n + 1):
        # คำนวณช่องว่างกับตัวอักษร
        space = ' ' * (n - i)
        step = pattern * i
        result.append(space + step)
    
    # เอาแต่ละบรรทัดมาต่อกันด้วย \n
    return '\n'.join(result)
