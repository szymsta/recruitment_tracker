# Libraries
import sys
import json
from datetime import datetime
import re
from tabulate import tabulate


# Path offers
path = "offers.json"
except_sign = f"{'*' * 40}"


# Load the offers from the file
def load_offers():
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save the offers to the file
def save_offers(offers):
    with open(path, "w", encoding="UTF-8") as file:
        json.dump(offers, file, indent=4)


# Main function to initialize and run the script
def main():
    global offers
    offers = load_offers()

    while True:
        welcome()
        choice = input("Enter your choice (1-5): ").strip()
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


# Get input data from user
def get_input():
    url = input("URL for the offer: ").strip()
    position = input("Position I applied for: ").strip()
    company = input("Company name: ").strip()
    date = input("Application date (YYYY-MM-DD): ").strip()
    salary_min = input("Minimum salary (only numbers): ").strip()
    salary_max = input("Maximum salary (only numbers): ").strip()

    return url, position, company, date, salary_min, salary_max

# Validate url format
def validate_url_format(your_url):
    while True:
        if re.match(r"^(https?:\/\/|www\.)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$", your_url):
            return your_url
        else:
            print("\nInvalid url, please provide correct one")
            your_url = input("URL for the offer: ").strip()

# Validate date format
def validate_date_format(your_date):
    while True:
        try:
            datetime.strptime(your_date, "%Y-%m-%d")
            return your_date
        except ValueError:
            print(f"\nInvalid date format: '{your_date}'. Enter correct date 'YYYY-MM-DD'")
            your_date = input("Application date (YYYY-MM-DD): ").strip()

# Validate salary amount
def validate_salary_amount(your_salary):
    while True:
        if your_salary.isnumeric() and int(your_salary) > 0:
            return your_salary
        else:
            print("\nSalary must be a positive number. Try again")
            your_salary = input("Minimum salary (only numbers): ").strip()


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
        print("\n" + except_sign)
        print("Invalid choice, Please try 1-5")
        print(except_sign)

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
    save_offers(offers)  # Save after actualization
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
        print("\n" + except_sign)
        print(f"No offers to show.")
        print(except_sign)


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

            save_offers(offers)  # Save after update

            print(f"\nOffer for '{position}' has been updated.")

        else:
            print("\n" + except_sign)
            print("Invalid number. No changes made.")
            print(except_sign)

    except ValueError:
        print("\n" + except_sign)
        print("Invalid input. Please enter a number.")
        print(except_sign)


# Select and remove the offer
def remove_offer():

    show_offer()

    try:
        index = int(input("Enter the number of the offer you want to remove: ")) - 1
        if 0 <= index < len(offers):
            removed = offers.pop(index)
            save_offers(offers) # Save after update
            print(f"Offer for '{removed['position']}' has been removed.")
        else:
            print("\n" + except_sign)
            print("Invalid number. No changes made.")
            print(except_sign)

    except ValueError:
        print("\n" + except_sign)
        print("Invalid input. Please enter a number.")
        print(except_sign)


# Run if main
if __name__ == "__main__":
    main()