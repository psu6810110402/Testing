def fizzbuzz(x: int) -> str:
    """
    รับค่าจำนวนเต็ม x แล้วคืนค่าตามเงื่อนไข:
    - หาร 3 และ 5 ลงตัว -> 'FizzBuzz'
    - หาร 3 ลงตัว        -> 'Fizz'
    - หาร 5 ลงตัว        -> 'Buzz'
    - กรณีอื่น            -> ตัวเลขนั้นในรูปแบบ string
    """
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)
