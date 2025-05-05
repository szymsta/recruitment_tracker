from tabulate import tabulate
from validator.validator import Validator
from offer_manager.input_handler import InputHandler
from config import Config


class OfferController:
    """
    The OfferController class manages operations related to job offers such as adding, showing,
    updating and removing offers.

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
    
    Constants:
        SUCCESS_MSG (str): Message displayed when an offer is successfully added, updated, or removed.
        ERROR_MSG (str): Message displayed when there's an error (e.g., invalid input).
        NO_OFFERS_MSG (str): Message displayed when there are no offers to display.
        OFFER_TABLE_HEADERS (list): The headers used to display the job offers table.
        SEPARATOR_LINE (str): A line used to separate different sections in the output.
    """


    def __init__(self, offers, file_manager):
        """
        Initializes the OfferController with a list of offers and a file manager instance.

        Args:
            file_manager (FileManager): An object to handle saving and loading offers from storage.
            offers (list): The list where job offers are stored.

        Notes:
            InputHandler is created directly here because it's a simple helper class.
            It handles collecting and checking user input when adding or updating offers.
        """
        self.file_manager = file_manager
        self.offers = offers
        self.input_handler = InputHandler()


    def add_offer(self):
        """
        Collects job offer details from the user and adds the offer to the list.

        The input is validated through the InputHandler. After successful validation, 
        the offer is appended to the internal list and saved using the file manager.
        """
        print("\nEnter the details for the offer you applied for:")

        try:
            # Step 1: Call the input handler to collect offer data from the user
            offer = self.input_handler.get_offer_input()

            # Step 2: Append the newly collected offer to the internal list of offers
            self.offers.append(offer)

            # Step 3: Save the updated list of offers to the file via the file manager
            self.file_manager.save_offers(self.offers)

            # Step 4: Inform the user that the offer has been successfully added
            print(f"\nOffer for '{offer['position']}' has been added.")

        except ValueError as e:

            # If there's an issue with the input (e.g., invalid data), print an error message
            print(f"Error: {e}")


    def show_offers(self):
        """
        Displays all job offers in a formatted table.

        Uses the `tabulate` library to format the data for readability.
        If no offers are found, a message is displayed instead.
        """
        if self.offers:
            # Step 1: Set the headers for the table from the Config file
            headers = Config.OFFER_TABLE_HEADERS

            # Step 2: Prepare the data for the table by iterating through all offers
            table = [
            [i + 1, o[Config.OFFER_KEYS["position"]], o[Config.OFFER_KEYS["company"]], 
             o[Config.OFFER_KEYS["link"]], o[Config.OFFER_KEYS["date"]], 
             o[Config.OFFER_KEYS["salary_min"]], o[Config.OFFER_KEYS["salary_max"]]] 
            for i, o in enumerate(self.offers)
            ]

            # Step 3: Display the table using the `tabulate` library with the specified format
            print(tabulate(table, headers=headers, tablefmt=Config.TABLE_FORMAT))

        else:
            # If no offers are available, inform the user
            print("\n" + Config.SEPARATOR_LINE_STAR)
            print("No offers to show.")
            print(Config.SEPARATOR_LINE_STAR)


    def update_offer(self):
        """
        Allows the user to update details of an existing job offer.

        First displays all current offers. The user selects an offer to update by index.
        Each field can be optionally updated by entering new data or left unchanged.
        """
        # Step 1: Display all current job offers
        self.show_offers()

        try:
            # Step 2: Prompt the user to select an offer by its number (index)
            index = int(input("Enter the number of the offer you want to update: ")) - 1

            # Step 3: Check if the index is valid (i.e., the offer exists in the list)
            if 0 <= index < len(self.offers):
                offer = self.offers[index]
                print("\nEnter new details (leave blank to keep current):")

                # Step 4: Prompt the user to input new values for each offer detail.
                # If the user leaves the input blank, the current value is kept.
                offer[Config.OFFER_KEYS["link"]] = input(f"Link (current: {offer[Config.OFFER_KEYS['link']]}): ") or offer[Config.OFFER_KEYS["link"]]
                offer[Config.OFFER_KEYS["position"]] = input(f"Position (current: {offer[Config.OFFER_KEYS['position']]}): ") or offer[Config.OFFER_KEYS["position"]]
                offer[Config.OFFER_KEYS["company"]] = input(f"Company (current: {offer[Config.OFFER_KEYS['company']]}): ") or offer[Config.OFFER_KEYS["company"]]
                offer[Config.OFFER_KEYS["date"]] = input(f"Date (current: {offer[Config.OFFER_KEYS['date']]}): ") or offer[Config.OFFER_KEYS["date"]]
                offer[Config.OFFER_KEYS["salary_min"]] = input(f"Min salary (current: {offer[Config.OFFER_KEYS['salary_min']]}): ") or offer[Config.OFFER_KEYS["salary_min"]]
                offer[Config.OFFER_KEYS["salary_max"]] = input(f"Max salary (current: {offer[Config.OFFER_KEYS['salary_max']]}): ") or offer[Config.OFFER_KEYS["salary_max"]]

                # Step 5: Save the updated list of offers to the file
                self.file_manager.save_offers(self.offers)

                # Step 6: Inform the user that the offer has been successfully updated
                print(f"Offer '{offer['position']}' updated.")

            else:
                # If the user entered an invalid index, print an error message
                print("Invalid number.")
        except ValueError:
            # If the input is not a valid integer, print an error message
            print("Invalid input.")


    def remove_offer(self):
        """
        Removes a selected job offer based on user input.

        First displays all current offers. The user selects an offer to remove by index.
        The selected offer is deleted from the list and changes are saved.
        """
        # Step 1: Display all current job offers
        self.show_offers()

        try:
            # Step 2: Prompt the user to select an offer to remove by entering its number (index)
            index = int(input("Enter the number of the offer you want to remove: ")) - 1

            # Step 3: Check if the entered index is valid (i.e., the offer exists in the list)
            if 0 <= index < len(self.offers):

                # Step 4: Remove the offer from the list using the pop method
                removed = self.offers.pop(index)

                # Step 5: Save the updated list of offers to the file
                self.file_manager.save_offers(self.offers)

                # Step 6: Inform the user that the offer has been successfully removed
                print(f"Removed offer '{removed['position']}'")

            else:
                # If the user enters an invalid index, print an error message
                print("Invalid number.")

        except ValueError:
            # If the input is not a valid integer, print an error message
            print("Invalid input.")
