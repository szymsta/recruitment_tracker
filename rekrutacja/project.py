# Libraries
import sys
import json


# Path offers
path = "offers.json"


# Load the offers
def load_offers():
    try:
        with open(path, "r", encoding = "UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Main function to initialize and run the script
def main():
    global offers
    offers = load_offers()

    while True:
        welcome()
        choice = input("Enter your choice (1-5): ").strip()
        choices(choice)


# Print menu function
def welcome():

    print(f"\n{'*' * 30}")
    print("Recruitment tracker")
    print(f"{'*' * 30} \n")
    print("Press number to choice what you want to do:")
    print("1. Add an offer I applied for")
    print("2. Remove an offer I applied for")
    print("3. Update an offer I applied for")
    print("4. Show all offers I applied for")
    print("5. Exit program")


# The function handling "user's" choice
def choices(item):

    if item == "1":
        add_offer()

    elif item == "2":
        pass

    elif item == "3":
        update_offer()

    elif item == "4":
        show_offer()

    elif item == "5":
        print("Exiting the program. All changes have been saved. Goodbye!")
        sys.exit()

    else:
        print("Invalid choice, Please try 1-5")


def add_offer():

    # Details from user:
    print("\nEnter the details for the offer you applied for:")

    url = input("URL for the offer: ")
    position = input("Position I applied for: ")
    company = input("Company name: ")
    date = input("Application date (YYYY-MM-DD): ")
    salary_min = float(input("Minimum salary (only numbers): "))
    salary_max = float(input("Maximum salary (only numbers): "))


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
    print(f"\nOffer for '{position}' has been added.")


# Show the offers that user applied for
def show_offer():

    if offers:
        print("\n--- Offers you applied for ---")
        for item, offer in enumerate(offers, start=1):
            print(f"{item}. Position: {offer['position']}")
            print(f"   Company: {offer["company"]}")
            print(f"   Link: {offer['link']}")
            print(f"   Application Date: {offer['date']}")
            print(f"   Salary Range: {offer['salary_min']:,} PLN - {offer['salary_max']:,} PLN")
            print("-" * 30)
    else:
        print(f"\nNo offers to show.\n")


# Update the offer
def update_offer():
    
    show_offer()

    try:
        index = int(input("Enter the number of the offer you want to update: ")) - 1
        if 0 <= index < len(offers):
            print("\nEnter new details for the selected offer:")
            link = input(f"Link (current: {offers[index]['link']}): ")
            position = input(f"Position (current: {offers[index]['position']}): ")
            date = input(f"Application date (current: {offers[index]['date']}): ")
            salary_min = input(f"Minimum salary (current: {offers[index]['salary_min']}): ")
            salary_max = input(f"Maximum salary (current: {offers[index]['salary_max']}): ")

            offers[index] = {
                "link": link,
                "position": position,
                "date": date,
                "salary_min": salary_min,
                "salary_max": salary_max
            }
            #save_offers()  # Zapisz oferty po aktualizacji
            print(f"\nOffer for '{position}' has been updated.")
        else:
            print("Invalid number. No changes made.")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()