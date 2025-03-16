import re

BIN_RE = re.compile(r'^[01]*$')

def bin_to_octal(bin_string: str) -> str:
    if not bin_string:
        return ''
    if not BIN_RE.match(bin_string):
        raise ValueError('Non-binary value was passed to the function')
    num = int(bin_string, 2)
    return oct(num)[2:] if num != 0 else '0'