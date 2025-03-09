def product_of_list_elements(lst):
    """
    Returns a new list where each element is the product of the preceding elements in the input list.
    """
    if not lst:
        return []

    # Initialize the result list and a running product variable
    result = [1] * len(lst)
    running_product = 1

    # Calculate the product of elements from the start
    for i in range(1, len(lst)):
        running_product *= lst[i - 1]
        result[i] = running_product

    # The result should not include the last element since there are no preceding elements for it
    return result[:-1]