from tabulate import tabulate
from validator.validator import Validator
from offer_manager.input_handler import InputHandler
from config import Config


class OfferController:

        def __init__(self, offers, file_manager):
        self.offers = offers
        self.file_manager = file_manager
        self.input_handler = InputHandler()


    def add_offer(self):
        print("\nEnter the details for the offer you applied for:")

        try:
            offer = self.input_handler.get_offer_input()
            self.offers.append(offer)
            self.file_manager.save_offers(self.offers)
            print(f"\nOffer for '{offer['position']}' has been added.")
        except ValueError as e:
            print(f"Error: {e}")


    def show_offers(self):
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