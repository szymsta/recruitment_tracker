class Config:
    """
    The Config class holds all configuration values and constants used throughout the application.

    This class centralizes the management of configurable parameters and default settings, making it easier to adjust
    the application behavior in a single location. The configuration includes settings for file management, URL and
    date validation patterns, error messages, prompts for user input, and offer-related keys.

    Attributes:
        FILE_PATH (str): The path to the file where job offers are stored (default is "offers.json").
        DEFAULT_ENCODING (str): The default encoding for reading and writing files (default is "UTF-8").
        FILE_READ_MODE (str): The file read mode (default is "r").
        FILE_WRITE_MODE (str): The file write mode (default is "w").
        SEPARATOR_LINE_STAR (str): A string of 40 asterisks used as a separator in output.
        SEPARATOR_LINE_EQUAL (str): A string of 30 equal signs followed by a newline, used as a separator.
        FILE_INDENT (int): The indentation level (default is 4) for JSON file writing.
        
        URL_PATTERN (str): A regular expression pattern used for validating URLs.
        DATE_FORMAT (str): The format for validating and parsing dates ("YYYY-MM-DD").
        SALARY_ERROR_MSG (str): The error message shown when an invalid salary is entered.
        URL_ERROR_MSG (str): The error message shown when an invalid URL is entered.
        DATE_ERROR_MSG (str): The error message shown when an invalid date format is entered.
        
        PROMPT_URL (str): The prompt message for entering a URL.
        PROMPT_POSITION (str): The prompt message for entering a job position.
        PROMPT_COMPANY (str): The prompt message for entering a company name.
        PROMPT_DATE (str): The prompt message for entering a date.
        PROMPT_SALARY_MIN (str): The prompt message for entering the minimum salary.
        PROMPT_SALARY_MAX (str): The prompt message for entering the maximum salary.
        
        OFFER_KEYS (dict): A dictionary mapping job offer keys to their corresponding field names.
        OFFER_TABLE_HEADERS (list): A list of headers for displaying job offers in a table.
        TABLE_FORMAT (str): The format used by the tabulate library for displaying tables (default is "pretty").
    """

    # file_manager
    FILE_PATH = "offers.json"
    DEFAULT_ENCODING  = "UTF-8"
    FILE_READ_MODE = "r"
    FILE_WRITE_MODE = "w"
    SEPARATOR_LINE_STAR = "*" * 40
    SEPARATOR_LINE_EQUAL = "=" * 30 + "\n"
    FILE_INDENT = 4


    # validation
    URL_PATTERN = r"^(https?://|www\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
    DATE_FORMAT = "%Y-%m-%d"
    SALARY_ERROR_MSG = "Salary must be a positive number."
    URL_ERROR_MSG = "Invalid URL. Try again."
    DATE_ERROR_MSG = "Invalid date format. Use YYYY-MM-DD."

    PROMPT_URL = "URL: "
    PROMPT_POSITION = "Position: "
    PROMPT_COMPANY = "Company: "
    PROMPT_DATE = "Date (YYYY-MM-DD): "
    PROMPT_SALARY_MIN = "Minimum salary: "
    PROMPT_SALARY_MAX = "Maximum salary: "


    # offer_controler
    OFFER_KEYS = {
    "position": "position",
    "company": "company",
    "link": "link",
    "date": "date",
    "salary_min": "salary_min",
    "salary_max": "salary_max",
    }

    OFFER_TABLE_HEADERS = [
    "#", 
    OFFER_KEYS["position"], 
    OFFER_KEYS["company"], 
    OFFER_KEYS["link"], 
    OFFER_KEYS["date"], 
    OFFER_KEYS["salary_min"], 
    OFFER_KEYS["salary_max"]
    ]

    TABLE_FORMAT = "pretty"