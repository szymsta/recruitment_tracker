# Libraries
import sys
import json
import re
from tabulate import tabulate

# Internal Modules
from config import Config
from file_manager.file_manager import FileManager


# Main function to initialize and run the script
def main():
    # Step1: Create an instance of the FileManager class with the file path from config
    file_manager = FileManager(Config.FILE_PATH)
    # Step 2: Declare 'offers' as a global variable so it can be accessed outside this function
    global offers
    # Step 3: Load offers from the file using the FileManager and assign them to the 'offers' variable
    offers = file_manager.load_offers()
    

    # Infinite loop to keep the program running until the user chooses to exit
    while True:
        # Step1: Display a welcome message or menu
        welcome()
        # Step 2: Prompt the user to enter their choice and remove leading/trailing whitespace
        choice = input("Enter your choice (1-5): ").strip()
        # Step 3: Handle the user's choice (e.g., show offers, add new one, etc.)
        choices(choice)


# Display the menu choices
def welcome():
    print(f"\n{'=' * 30}")
    print("Recruitment tracker")
    print(f"{'=' * 30}\n")
    print("Press a number to choose what you want to do:")
    print("    1. Add an offer I applied for")
    print("    2. Remove an offer I applied for")
    print("    3. Update an offer I applied for")
    print("    4. Show all offers I applied for")
    print("    5. Exit program")


# The function handling "user's" choice
def choices(item):
    if item == "1":
        add_offer()
    elif item == "2":
        remove_offer()
    elif item == "3":
        update_offer()
    elif item == "4":
        show_offer()
    elif item == "5":
        print("Exiting the program. All changes have been saved. Goodbye!")
        sys.exit()
    else:
        print("\n" + Config.SEPARATOR_LINE_STAR)
        print("Invalid choice, Please try 1-5")
        print(Config.SEPARATOR_LINE_STAR)

# Add a new offer
def add_offer():
    print("\nEnter the details for the offer you applied for:")

    try:
        url, position, company, date, salary_min, salary_max = get_input() # Get details from user

        # Validate data
        url = validate_url_format(url)
        date = validate_date_format(date)
        salary_min = validate_salary_amount(salary_min)
        salary_max = validate_salary_amount(salary_max)

        print(f"Offer for position '{position}' at company '{company}' has been added.")

    except ValueError as e:
        print(f"Error: {e}")
        return

    # Create dict for offer
    offer = {
        "link": url,
        "position": position,
        "company": company,
        "date": date,
        "salary_min": salary_min,
        "salary_max": salary_max
    }
    
    # Add offer to offers list
    offers.append(offer)
    file_manager.save_offers(offers)  # Save after actualization
    print(f"\nOffer for '{position}' has been added.")


# Show the offers that user applied for
def show_offer():

    if offers:
        headers = ["#","Position", "Company", "Link", "Application Date", "Salary Min", "Salary Max"]
        table = []

        for item, offer in enumerate(offers, start=1):
            table.append([
                item,
                offer['position'],
                offer['company'],
                offer['link'],
                offer['date'],
                offer['salary_min'],
                offer['salary_max']
            ])

        print(tabulate(table, headers=headers, tablefmt="pretty"))

    else:
        print("\n" + Config.SEPARATOR_LINE_STAR)
        print(f"No offers to show.")
        print(Config.SEPARATOR_LINE_STAR)


# Update the offer
def update_offer():
    
    show_offer()

    try:
        index = int(input("Enter the number of the offer you want to update: ").strip()) - 1

        if 0 <= index < len(offers):
            print("\nEnter new details for the selected offer:")

            link = input(f"Link (current: {offers[index]['link']}): ").strip()
            position = input(f"Position (current: {offers[index]['position']}): ").strip()
            company = input(f"Company (current: {offers[index]['company']}): ").strip()
            date = input(f"Application date (current: {offers[index]['date']}): ").strip()
            salary_min = float(input(f"Minimum salary (current: {offers[index]['salary_min']}): ").strip())
            salary_max = float(input(f"Maximum salary (current: {offers[index]['salary_max']}): ").strip())

            offers[index] = {
                "link": link,
                "position": position,
                "company": company,
                "date": date,
                "salary_min": salary_min,
                "salary_max": salary_max
            }

            file_manager.save_offers(offers)  # Save after update

            print(f"\nOffer for '{position}' has been updated.")

        else:
            print("\n" + Config.SEPARATOR_LINE_STAR)
            print("Invalid number. No changes made.")
            print(Config.SEPARATOR_LINE_STAR)

    except ValueError:
        print("\n" + Config.SEPARATOR_LINE_STAR)
        print("Invalid input. Please enter a number.")
        print(Config.SEPARATOR_LINE_STAR)


# Select and remove the offer
def remove_offer():

    show_offer()

    try:
        index = int(input("Enter the number of the offer you want to remove: ")) - 1
        if 0 <= index < len(offers):
            removed = offers.pop(index)
            file_manager.save_offers(offers) # Save after update
            print(f"Offer for '{removed['position']}' has been removed.")
        else:
            print("\n" + Config.SEPARATOR_LINE_STAR)
            print("Invalid number. No changes made.")
            print(Config.SEPARATOR_LINE_STAR)

    except ValueError:
        print("\n" + Config.SEPARATOR_LINE_STAR)
        print("Invalid input. Please enter a number.")
        print(Config.SEPARATOR_LINE_STAR)


# Run if main
if __name__ == "__main__":
    main()