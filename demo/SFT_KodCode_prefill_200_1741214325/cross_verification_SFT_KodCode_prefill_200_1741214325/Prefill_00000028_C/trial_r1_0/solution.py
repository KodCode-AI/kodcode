import re

def is_valid_double(s: str) -> bool:
    """
    Returns True if the given string is a valid double, False otherwise.
    """
    pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
    return bool(re.fullmatch(pattern, s))

# To test:
# Cases it handles correctly:
print(is_valid_double("123"))             # True
print(is_valid_double("-123.45"))         # True
print(is_valid_double("+123e5"))          # True
print(is_valid_double("123."))            # True

# Cases it doesn't handle:
print(is_valid_double("inf"))             # Should be True but returns False
print(is_valid_double("nan"))             # Should be True but returns False
print(is_valid_double("+inf"))            # Should be True but returns False
print(is_valid_double("0x1f"))            # Should be True but returns False
print(is_valid_double("123e"))            # False correctly as per the pattern
print(is_valid_double("e5"))              # False correctly as per the pattern
print(is_valid_double("."))               # False correctly