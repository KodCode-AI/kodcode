def find_next_power_of_two(number: int) -> int:
    return 1 << number.bit_length()