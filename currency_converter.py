"""Currency converter

This application converts currency based on exchange rates
published by European Central Bank.

Module `forex_python` is required to be installed
within the Python environment you are running this in.

Created by Samuel Mensak.

"""

import json
import argparse
import forex_python.converter


def symbol_converter(currency: str) -> str:
    """Function converts currency symbol to 3 letter code.

    Args:
        currency: Currency code to be converted.

    Returns:
        3 letter currency code.

    """
    return {
        "$": "USD",
        "€": "EUR",
        "£": "GBP",
        "¥": "JPY",
        "R": "ZAR",
        "฿": "THB",
        "₱": "PHP",
        "₽": "RUB",
        "₩": "KRW",
        "₪": "ILS",
        "RM": "MYR",
        "Rp": "IDR",
        "R$": "BRL",
        "kn": "HRK",
        "zł": "PLN",
        "Ft": "HUF",
        "Kč": "CZK",
        "лв": "BGN",
        "lei": "RON",
    }.get(currency, currency)


def fatal_error(msg: str):
    """Function prints given message and exits program."""
    print(msg)
    exit(1)


def main(args):
    # argument parser setup
    parser = argparse.ArgumentParser(description='currency converter')

    parser.add_argument('-a', '--amount', type=float,
                        help='Amount to convert', required=True)
    parser.add_argument('-i', '--input_currency', type=str,
                        help='Currency to convert', required=True)
    parser.add_argument('-o', '--output_currency', type=str,
                        help='Currency to be converted to', required=False)

    if args:
        arguments = parser.parse_args(args)
    else:
        arguments = parser.parse_args()

    # get currency exchange rates
    converter = forex_python.converter.CurrencyRates()
    output = {}
    # check input arguments, convert symbols to 3 letter code
    if len(arguments.input_currency) > 3:
        fatalError("Invalid input currency!")
    else:
        input_currency = symbol_converter(arguments.input_currency)

    if arguments.output_currency:

        if len(arguments.output_currency) > 3:
            fatal_error("Invalid output currency!")
        else:
            output_currency = symbol_converter(arguments.output_currency)

        # convert input currency to desired output currency
        try:
            output[arguments.output_currency] = converter.convert(
                input_currency, output_currency, arguments.amount)
        except (forex_python.converter.RatesNotAvailableError,
                forex_python.converter.DecimalFloatMismatchError):
            fatal_error("Unable to convert, "
                        "chceck currency format or "
                        "if currency you've entered is supported.")

        output = {symbol_converter(key): round(value, 3)
                  for key, value in output.items()}

    else:
        # convert input currency to all availible currencies
        try:
            currency_dict = converter.get_rates(input_currency)
        except (forex_python.converter.RatesNotAvailableError,
                forex_python.converter.DecimalFloatMismatchError):
            fatal_error("Unable to convert, "
                        "chceck input currency format or "
                        "if currency you've entered is supported.")

        output = {key: round(value * arguments.amount, 3) for
                  key, value in currency_dict.items()}
        del output[input_currency]

    # print or return results in specified format
    result = json.dumps({
            "input": {
                "amount": arguments.amount,
                "currency": input_currency
            },
            "output": output
            }, indent=4)

    if args:
        return result
    else:
        print(result)


if __name__ == "__main__":
    main(None)
