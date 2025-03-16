def sum_of_even_numbers(numbers):
    total_sum = 0
    for number in numbers:
        if number % 2 == 0:
            total_sum += number
    return total_sum