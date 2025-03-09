def count_letters(n: int) -> int:
    """
    Returns the count of letters used when the number from 1 to 1000 is written in words.
    """
    if not 1 <= n <= 1000:
        raise ValueError("Input must be between 1 and 1000")

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]

    def count(n):
        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ("" if n % 10 == 0 else "-" + units[n % 10])
        elif n < 1000:
            return units[n // 100] + " hundred" + ("" if n % 100 == 0 else " and" + count(n % 100))
        else:
            return thousands[1] + count(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " and" + count(n % 1000))

    result = count(n)
    return len(result.replace(" ", "").replace("-", ""))