def find_pandigital_fibonacci() -> int:
    def check(number: int) -> bool:
        s = str(number)
        return ''.join(sorted(s)) == '123456789'

    def check1(number: int) -> bool:
        s = str(number)
        return ''.join(sorted(s[:9])) == '123456789' and ''.join(sorted(s[-9:])) == '123456789'

    F1, F2 = 0, 1
    index = 2
    while index < 1000000:
        F1, F2 = F2, (F1 + F2) % 1000000000000000000  # To handle large numbers
        if check(F2) and check1(F2):
            return index
        index += 1
    return -1