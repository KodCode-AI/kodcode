def find_next_power_of_two(number: int) -> int:
    if number == 0:
        return 1
    highest_bit = number.bit_length() - 1
    return 1 << (highest_bit + 1)