def sum_recursive(lst, index=0):
    if index == len(lst):
        return 0
    else:
        return lst[index] + sum_list(lst, index + 1)

# Example usage:
numbers = [1, 2, 3, 4, 5]
sum_result = sum_list(numbers)
print("Sum of the list:", sum_result)