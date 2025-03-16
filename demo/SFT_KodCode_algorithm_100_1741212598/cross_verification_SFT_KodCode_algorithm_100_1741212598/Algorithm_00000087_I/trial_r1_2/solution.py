def bin_to_octal(bin_string: str) -> str:
    if not bin_string:
        return ''
    for c in bin_string:
        if c not in {'0', '1'}:
            raise ValueError("Non-binary value was passed to the function")
    if bin_string.strip('0') == '':
        return '0'
    pad = (3 - (len(bin_string) % 3)) % 3
    padded = '0' * pad + bin_string
    octal_digits = []
    for i in range(0, len(padded), 3):
        chunk = padded[i:i+3]
        digit = str(int(chunk, 2))
        octal_digits.append(digit)
    octal_str = ''.join(octal_digits)
    stripped = octal_str.lstrip('0')
    return stripped if stripped else '0'