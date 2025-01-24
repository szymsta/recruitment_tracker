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
    print("*" * 30)
    print("Recruitment tracker")
    print("*" * 30)
    print("Press number to choice what you want to do:")
    print("1. Add an offer I applied for")
    print("2. Remove an offer I applied for")
    print("3. Update an offer I applied for")
    print("4. Show all offers I applied for")
    print("5. Exit program")


# 
def choices(item):

    if item == "1":
        add_offer()
    elif item == "2":
        pass
    elif item == "3":
        pass
    elif item == "4":
        pass
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
    date = input("Application date (YYYY-MM-DD): ")
    salary_min = input("Minimum salary: ")
    salary_max = input("Maximum salary: ")

    # Create dict for offer
    offer = {
        "link": url,
        "position": position,
        "date": date,
        "salary_min": salary_min,
        "salary_max": salary_max
    }

    # Add offer to offers list
    offers.append(offer)
    print(f"\nOffer for '{position}' has been added.")

if __name__ == "__main__":
    main()