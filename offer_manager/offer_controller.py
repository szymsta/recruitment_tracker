from tabulate import tabulate
from validator.validator import Validator
from offer_manager.input_handler import InputHandler
from config import Config


class OfferController:
    """
    The OfferController class manages operations related to job offers such as adding, displaying,
    updating, and removing offers.

    It interacts with the input handler to collect user data and with the file manager to persist changes.
    Offers are stored in memory as a list of dictionaries and synced with a file storage system.

    Attributes:
        offers (list): A list of dictionaries, each representing a job offer.
        file_manager (FileManager): An instance responsible for saving and loading offers.
        input_handler (InputHandler): Collects and validates user input for job offers.

    Methods:
        add_offer(): Collects input from the user, validates it, and adds a new job offer to the list.
        show_offers(): Displays all current job offers in a formatted table.
        update_offer(): Allows the user to update an existing job offer's fields.
        remove_offer(): Removes a selected job offer from the list based on user input.
    """

    def __init__(self, offers, file_manager):
        """
        Initializes the OfferController with a list of offers and a file manager instance.

        Args:
            offers (list): The list where job offers are stored.
            file_manager (FileManager): An object to handle saving and loading offers from storage.
        """
        self.offers = offers
        self.file_manager = file_manager
        self.input_handler = InputHandler()


    def add_offer(self):
         """
        Collects job offer details from the user and adds the offer to the list.

        The input is validated through the InputHandler. After successful validation, 
        the offer is appended to the internal list and saved using the file manager.
        """
        print("\nEnter the details for the offer you applied for:")

        try:
            offer = self.input_handler.get_offer_input()
            self.offers.append(offer)
            self.file_manager.save_offers(self.offers)
            print(f"\nOffer for '{offer['position']}' has been added.")
        except ValueError as e:
            print(f"Error: {e}")


    def show_offers(self):
        """
        Displays all job offers in a formatted table.

        Uses the `tabulate` library to format the data for readability.
        If no offers are found, a message is displayed instead.
        """
        if self.offers:
            headers = ["#", "Position", "Company", "Link", "Application Date", "Salary Min", "Salary Max"]
            table = [[i+1, o['position'], o['company'], o['link'], o['date'], o['salary_min'], o['salary_max']] 
                     for i, o in enumerate(self.offers)]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print("\n" + Config.SEPARATOR_LINE_STAR)
            print("No offers to show.")
            print(Config.SEPARATOR_LINE_STAR)


    def update_offer(self):
        """
        Allows the user to update details of an existing job offer.

        First displays all current offers. The user selects an offer to update by index.
        Each field can be optionally updated by entering new data or left unchanged.
        """
        self.show_offers()
        try:
            index = int(input("Enter the number of the offer you want to update: ")) - 1
            if 0 <= index < len(self.offers):
                offer = self.offers[index]
                print("\nEnter new details (leave blank to keep current):")

                offer['link'] = input(f"Link (current: {offer['link']}): ") or offer['link']
                offer['position'] = input(f"Position (current: {offer['position']}): ") or offer['position']
                offer['company'] = input(f"Company (current: {offer['company']}): ") or offer['company']
                offer['date'] = input(f"Date (current: {offer['date']}): ") or offer['date']
                offer['salary_min'] = input(f"Min salary (current: {offer['salary_min']}): ") or offer['salary_min']
                offer['salary_max'] = input(f"Max salary (current: {offer['salary_max']}): ") or offer['salary_max']

                self.file_manager.save_offers(self.offers)
                print(f"Offer '{offer['position']}' updated.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input.")


    def remove_offer(self):
        """
        Removes a selected job offer based on user input.

        First displays all current offers. The user selects an offer to remove by index.
        The selected offer is deleted from the list and changes are saved.
        """
        self.show_offers()
        try:
            index = int(input("Enter the number of the offer you want to remove: ")) - 1
            if 0 <= index < len(self.offers):
                removed = self.offers.pop(index)
                self.file_manager.save_offers(self.offers)
                print(f"Removed offer '{removed['position']}'")
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input.")
