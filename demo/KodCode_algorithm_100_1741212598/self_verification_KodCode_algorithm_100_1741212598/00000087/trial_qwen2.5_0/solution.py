def bin_to_octal(bin_string: str) -> str:
    if not bin_string or not set(bin_string).issubset({'0', '1'}):
        raise ValueError("Non-binary value was passed to the function")
    
    octal = ""
    dict = {4: "1", 5: "2", 6: "3", 7: "4", 0: "0", 1: "1", 2: "2", 3: "3"}
    count = 0
    for bit in reversed(bin_string):
        count = (count << 1) | int(bit)
        if count in dict:
            octal = dict[count] + octal
            count = 0
    return octal