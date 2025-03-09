from typing import List
import requests

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
    """
    try:
        # Check if the list is empty
        if not amounts:
            return "Error: The list of amounts is empty."

        # Make the API call with the minimum number of calls
        url = f"https://api.amdoren.com/currency/v1/convert"
        response = requests.post(
            url,
            params={
                "apikey": api_key,
                "from": from_currency,
                "to": to_currency
            },
            json={"amounts": amounts}
        )

        if response.status_code != 200:
            return "Error: The API call failed. Please check your internet connection or try again later."

        data = response.json()
        if 'results' not in data:
            return "Error: Invalid response from the API."

        # Format the output
        formatted_output = ", ".join([f"{amount}: {converted_amount} {to_currency}" for amount, converted_amount in zip(amounts, data['results'])])
        return formatted_output
    except Exception as e:
        return f"Error: {str(e)}"