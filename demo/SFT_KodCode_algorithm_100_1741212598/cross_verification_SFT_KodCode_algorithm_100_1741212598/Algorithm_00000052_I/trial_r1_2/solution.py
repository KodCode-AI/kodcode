def find_next_power_of_two(number: int) -> int:
    if number == 0:
        return 1
    return 1 << (number.bit_length())