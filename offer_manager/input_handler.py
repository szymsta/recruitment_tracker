from validator.validator import Validator
from config import Config


class InputHandler:
    def get_offer_input(self):
        url = Validator.validate_url(input(Config.PROMPT_URL))
        position = input(Config.PROMPT_POSITION).strip()
        company = input(Config.PROMPT_COMPANY).strip()
        date = Validator.validate_date(input(Config.PROMPT_DATE))
        salary_min = Validator.validate_salary(input(Config.PROMPT_SALARY_MIN))
        salary_max = Validator.validate_salary(input(Config.PROMPT_SALARY_MAX))

        return {
            "link": url,
            "position": position,
            "company": company,
            "date": date,
            "salary_min": salary_min,
            "salary_max": salary_max,
        }
