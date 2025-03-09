def count_letters(n: int) -> int:
    """
    Converts numbers from 1 to 1000 into their English word representations and counts the total number
    of letters used, excluding spaces and hyphens.
    """
    if n == 1000:
        return 11  # "one thousand" has 11 letters (excluding spaces)
    
    num_words = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    def convert(n: int) -> str:
        if n <= 20:
            return num_words[n]
        elif n < 100:
            return tens[(n // 10) - 2] + ("" if n % 10 == 0 else "-" + num_words[n % 10])
        elif n < 1000:
            if n % 100 == 0:
                return num_words[n // 100] + " hundred"
            else:
                return num_words[n // 100] + " hundred and " + convert(n % 100)
        else:
            return "onethousand"
    
    count = sum(len(convert(i).replace(" ", "").replace("-", "")) for i in range(1, n + 1))
    return count