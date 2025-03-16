def bin_to_octal(bin_string: str) -> str:
    if not bin_string:
        return ''
    for c in bin_string:
        if c not in ('0', '1'):
            raise ValueError("Non-binary value was passed to the function")
    decimal = int(bin_string, 2)
    return oct(decimal)[2:]