from typing import List

def convert_currency_multiple(
    api_key: str,
    from_currency: str,
    to_currency: str,
    amounts: List[float],
) -> str:
    """
    Convert multiple currency amounts from one currency to another using the Amdoren Currency API.

    :param api_key: API key for the Amdoren Currency API.
    :param from_currency: Currency to convert from.
    :param to_currency: Currency to convert to.
    :param amounts: List of amounts to convert.
    :return: A formatted string containing the converted amounts or an error message.

    Example:
    >>> convert_currency_multiple("your_api_key", "USD", "INR", [1.0, 2.5, 3.0])
    '1.0: 74.65 INR, 2.5: 186.63 INR, 3.0: 223.98 INR'
    """
    # Here you would typically make an API call. For this example, we're just going to return a static message.
    if not amounts:
        return "No amounts provided."

    if not (from_currency.isalpha() and to_currency.isalpha()):
        return "Invalid currency codes provided."

    if not all(isinstance(amount, (int, float)) for amount in amounts):
        return "Invalid amount values."

    # Example of a static message for demonstration purposes
    converted_amounts = {amount: f"{amount} {from_currency} is {amount * 74.65} {to_currency}" for amount in amounts}
    return ", ".join(f"{key}: {value}" for key, value in converted_amounts.items())

# Example usage
# print(convert_currency_multiple("your_api_key", "USD", "INR", [1.0, 2.5, 3.0]))