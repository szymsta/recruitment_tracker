# Libraries
import sys

# Internal Modules
from config import Config
from file_manager.file_manager import FileManager
from validator.validator import Validator
from offer_manager.input_handler import InputHandler
from offer_manager.offer_controller import OfferController


# Main function to initialize and run the script
def main():
    # Initialize core components
    file_manager = FileManager(Config.FILE_PATH)
    input_handler = InputHandler()
    offers = []
    
    # Create controller with required dependencies
    offer_controller = OfferController(offers, file_manager)

    # Infinite loop to keep the program running until the user chooses to exit
    while True:
        welcome()
        choice = input("Enter your choice (1-5): ").strip()
        choices(choice, offer_controller)


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
def choices(choice, offer_controller):
    if choice == "1":
        offer_controller.add_offer()
    elif choice == "2":
        offer_controller.remove_offer()
    elif choice == "3":
        offer_controller.update_offer()
    elif choice == "4":
        offer_controller.show_offers()
    elif choice == "5":
        print("Exiting the program. All changes have been saved. Goodbye!")
        sys.exit()
    else:
        print("\n" + Config.SEPARATOR_LINE_STAR)
        print("Invalid choice, Please try 1-5")
        print(Config.SEPARATOR_LINE_STAR)


# Run if main
if __name__ == "__main__":
    main()