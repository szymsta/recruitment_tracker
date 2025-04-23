class Config:

    FILE_PATH = "offers.json"
    DEFAULT_ENCODING  = "UTF-8"
    FILE_READ_MODE = "r"
    FILE_WRITE_MODE = "w"
    SEPARATOR_LINE_STAR = "*" * 40
    SEPARATOR_LINE_EQUAL = "=" * 30 + "\n"
    FILE_INDENT = 4


    URL_PATTERN = r"^(https?://|www\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
    DATE_FORMAT = "%Y-%m-%d"
    SALARY_ERROR_MSG = "Salary must be a positive number."
    URL_ERROR_MSG = "Invalid URL. Try again."
    DATE_ERROR_MSG = "Invalid date format. Use YYYY-MM-DD."