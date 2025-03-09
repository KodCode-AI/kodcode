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
    """
    if not amounts:
        return "Error: No amounts provided"

    try:
        import requests
    except ImportError:
        return "Error: Missing required package 'requests'"

    base_url = "https://api.amdoren.com/api/v1/convert"
    params = {
        "apikey": api_key,
        "from": from_currency,
        "to": to_currency,
        "amounts": ",".join(map(str, amounts))
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return f"Error: API request failed with status {response.status_code}"

    data = response.json()
    if data.get("error"):
        return data["error"]

    converted_amounts = []
    for amount, converted in zip(amounts, data["converted"]):
        converted_amounts.append(f"{amount}: {converted} {to_currency}")

    return ", ".join(converted_amounts)