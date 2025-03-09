def find_pandigital_fibonacci() -> int:
    def check(number: int) -> bool:
        return sorted(str(number)) == list('123456789')
    
    def check1(number: int) -> bool:
        return sorted(str(number)) == list('123456789')[::-1]
    
    first, second = 1, 1
    index = 2
    while index <= 1000000:
        number = first + second
        if check(number) and check1(number):
            return index
        first, second = second, number
        index += 1
    return -1