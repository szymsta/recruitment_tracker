from validator.validator import Validator
from config import Config


class InputHandler:
    """
    The InputHandler class is responsible for collecting user input related to job offers.

    It prompts the user for various fields such as URL, position, company name, date, and salary range,
    and validates the input using methods from the `Validator` module.

    Attributes:
        None

    Methods:
        get_offer_input(): Prompts the user for job offer details, validates the input,
        and returns the data as a dictionary.

    Constants:
        PROMPT_URL (str): The prompt message for the URL input.
        PROMPT_POSITION (str): The prompt message for the position input.
        PROMPT_COMPANY (str): The prompt message for the company input.
        PROMPT_DATE (str): The prompt message for the date input.
        PROMPT_SALARY_MIN (str): The prompt message for the minimum salary input.
        PROMPT_SALARY_MAX (str): The prompt message for the maximum salary input.

    Args:
        None
    """
    def get_offer_input(self):
        """
        Collects and validates user input for a job offer.

        Prompts the user to enter values for URL, position, company, date, minimum salary, and maximum salary. 
        Each input is validated using corresponding methods from the `Validator` class. The prompts for input are 
        defined in the `Config` module.

        Returns: dict: A dictionary containing validated job offer information with the following keys:
                - "link" (str): Validated job offer URL.
                - "position" (str): Job position entered by the user.
                - "company" (str): Company name entered by the user.
                - "date" (str): Validated date string.
                - "salary_min" (float or int): Validated minimum salary.
                - "salary_max" (float or int): Validated maximum salary.
        """
        # Step 1: Collect user input for job offer details using prompts defined in Config
        url = Validator.validate_url(input(Config.PROMPT_URL))
        position = input(Config.PROMPT_POSITION).strip()
        company = input(Config.PROMPT_COMPANY).strip()
        date = Validator.validate_date(input(Config.PROMPT_DATE))
        salary_min = Validator.validate_salary(input(Config.PROMPT_SALARY_MIN))
        salary_max = Validator.validate_salary(input(Config.PROMPT_SALARY_MAX))

        # Step 2: Return a dictionary containing the validated input data
        return {
            "link": url,
            "position": position,
            "company": company,
            "date": date,
            "salary_min": salary_min,
            "salary_max": salary_max,
        }
