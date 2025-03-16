def is_even(number: int) -> bool:
    """Determine if a number is even using bitwise operators."""
    return not (number & 1)