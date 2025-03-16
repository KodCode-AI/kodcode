def count_trailing_zeros(n):
    def count_factor(n, factor):
        count = 0
        while n % factor == 0 and n != 0:
            count += 1
            n = n // factor
        return count
    
    count_2 = count_factor(n, 2)
    count_5 = count_factor(n, 5)
    
    return min(count_2, count_5)

# Example usage:
print(count_trailing_zeros(100))  # Output: 2
print(count_trailing_zeros(1000))  # Output: 3
print(count_trailing_zeros(5))     # Output: 1
print(count_trailing_zeros(8))     # Output: 0