# Libraries
import re
from datetime import datetime

# Internal modules
from config import Config


class Validator:
    """
    The Validator class provides static methods to validate various types of user input related to job offer data.

    It includes validation for URLs, date formats, and salary values. All methods ensure that the data provided by the user
    meets the expected format or type requirements, prompting re-entry if validation fails.

    Attributes:
        None

    Methods:
        validate_url(url): Validates the format of a URL string. Prompts user until a valid URL is provided.
        validate_date(date_str): Validates the format of a date string in 'YYYY-MM-DD' format. Prompts user until a valid date is entered.
        validate_salary(salary): Validates that the input is a positive numeric string. Prompts user until a valid salary is provided.

    Constants:
        URL_PATTERN (str): Regular expression pattern for validating URLs.
        DATE_FORMAT (str): The date format used for validating date strings.
        SALARY_ERROR_MSG (str): The error message displayed when a non-positive salary is entered.
        URL_ERROR_MSG (str): The error message displayed when an invalid URL is entered.
        DATE_ERROR_MSG (str): The error message displayed when an invalid date is entered.

    Args:
        None
    """


    @staticmethod
    def validate_url(your_url):
        """
        Validates the format of the given URL.

        Uses a regular expression to check if the input string matches a valid URL pattern.
        If the URL is not valid, the user is prompted to re-enter the URL until a correct format is provided.

        Args:
            your_url (str): The URL to validate.

        Returns:
            str: A validated URL string that matches the expected pattern.
        """
        # Loop until the URL matches the configured regex
        while not re.match(Config.URL_PATTERN, your_url): 
            print(Config.URL_ERROR_MSG)
            your_url = input("URL: ").strip()
        return your_url


    @staticmethod
    def validate_date(your_date):
        """
        Validates the format of the given date string.

        Attempts to parse the input using the 'YYYY-MM-DD' format. If parsing fails,
        the user is prompted to re-enter the date until a valid date is provided.

        Args:
            your_date (str): The date string to validate.

        Returns:
            str: A validated date string in 'YYYY-MM-DD' format.
        """
        while True:
            try:
                datetime.strptime(your_date, Config.DATE_FORMAT)
                return your_date
            except ValueError:
                print(Config.DATE_ERROR_MSG)
                your_date = input("Date (YYYY-MM-DD): ").strip()


    @staticmethod
    def validate_salary(your_salary):
        """
        Validates that the salary input is a positive number.

        Ensures that the input string represents a positive integer.
        If the input is not a valid positive number, the user is prompted to re-enter it.

        Args:
            your_salary (str): The salary input to validate.

        Returns:
            str: A validated string representing a positive numeric salary.
        """
        while not your_salary.isdigit() or int(your_salary) <= 0:
            print(Config.SALARY_ERROR_MSG)
            your_salary = input("Salary: ").strip()
        return your_salary