def count_letters(n: int) -> int:
    """
    Converts numbers from 1 to 1000 into their English word representations and counts the total number of letters used,
    excluding spaces and hyphens.
    """
    assert 1 <= n <= 1000, "Input must be between 1 and 1000"
    
    # Helper words
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]
    
    def number_to_words(num):
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else '-' + ones[num % 10])
        elif num < 1000:
            return ones[num // 100] + " hundred" + ('' if num % 100 == 0 else ' and ' + number_to_words(num % 100))
        else:
            return number_to_words(num // 1000) + ' thousand ' + number_to_words(num % 1000)
    
    words = number_to_words(n)
    return len(words.replace(" ", "").replace("-", ""))