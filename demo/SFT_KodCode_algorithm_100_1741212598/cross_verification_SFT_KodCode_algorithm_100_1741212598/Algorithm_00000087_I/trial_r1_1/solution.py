def bin_to_octal(bin_string: str) -> str:
    if not bin_string:
        return ''
    try:
        n = int(bin_string, 2)
    except ValueError:
        raise ValueError("Non-binary value was passed to the function")
    return oct(n)[2:]