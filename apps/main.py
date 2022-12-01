"""
Represent a data-set of Exchange_Rates

Authors:
  - https://github.com/bj1057
  - https://github.com/ns1270

Implementation requirements:
   1. MUST use a for ... in ... loop
   1. MUST NOT use list comprehensions
   2. MUST NOT use lambda functions
   3. MUST NOT call built-in functions or methods that
      eliminate the use of a for loop
   4. MUST NOT use for ... in ... range(len(...))
"""
import sys


class ExchangeRates:
    """
    Represent a data-set of Exchange Rates Information of different countries.

    Concepts:
        Data processing functionality.
        Reading and writing from CSV files.
    """
    def __int__(self, exchange_rate_info: list):
        """
        Create and initialize the class attributes.

        Attributes: a list of tuples of:
            exchange_rate: integer
            date: string
            currency_name: 3-character string
        """
        self.exchange_rate_info = exchange_rate_info

    def write(self, filename: str):
        """
        Write a CSV file with exchange rates data.

        A record is a row in the file, with three columns, corresponding to
        date,exchange rate,exchange currency

        filename: filename to write data to
        """

    def exchange_rates_by_country(self) -> dict:
        """
        Getting Information of exchange rate of Indian Rupee and US dollar based upon the particular date.

        Return: nested dictionary with currency exchange rate values of Indian Rupee and US dollar based upon the particular date.
        Dictionary
             keys: string, each representing a particular date
             values:Nested dictionary of currency_name,currency_value
        Nested Dictionary
            keys: string, each representing a Currency name
            values:integer, currency values of that particular country
        """

    def exchange_rates_range_by_dates(self) -> list:
        """
        Create a lookup of exchange rates of each country in range of date

        Return: List of dictionaries, dictionary with
            keys: string, each representing a Currency name
            values: currency values of that particular country
        """

    def exchangerate_by_date(self) -> dict:
        """
        Create a lookup of currency exchange rate values are extracted based upon the date

        Return: nested dictionary with currency exchange rate values based upon the date.
        Dictionary
             keys: string, each representing a particular date
             values:Nested dictionary of currency_name,currency_value
        Nested Dictionary
            keys: string, each representing a Currency name
            values:integer, currency values of that particular country
        """

    def read_dataset(filename: str) -> ExchangeRates:
        """
        Read a CSV text file that holds 3-element records,where each has name.

        currency_name, and currency_value of exchange rates.
        Need to create an empty list.
        Use the file open method with reading mode.

        Return the list of tuples of exchangerates.
        """


def main():
    """
    Run the sample code.

    (Tests are in different modules.)
    """


if __name__ == '__main__':
    main()
