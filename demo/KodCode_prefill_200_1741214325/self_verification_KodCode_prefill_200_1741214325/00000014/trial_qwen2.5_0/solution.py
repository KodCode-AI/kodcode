def product_of_list_elements(lst):
    """
    Returns a new list where each element is the product of preceding elements from the input list.
    """
    if not lst:
        return []
    
    result = []
    product = 1
    for num in lst:
        result.append(product)
        product *= num
    return result