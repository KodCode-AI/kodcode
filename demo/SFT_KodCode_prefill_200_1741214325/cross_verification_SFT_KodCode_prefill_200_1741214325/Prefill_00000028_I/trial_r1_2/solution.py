def is_valid_double(s):
    if '.' not in s:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False