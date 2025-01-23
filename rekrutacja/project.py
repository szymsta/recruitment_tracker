import sys


def main():
    while True:
        welcome()
        choice = input("Enter your choice (1-5): ").strip()
        menu(choice)


def welcome():
    print("*" * 30)
    print("Welcom to recruitment tracker")
    print("*" * 30)
    print("Press number to choice what you want to do:")
    print("1. Add an offer I applied for")
    print("2. Remove an offer I applied for")
    print("3. Update an offer I applied for")
    print("4. Show all offers I applied for")
    print("5. Exit program")


def menu(item):
    if item == "1":
        pass
    elif item == "2":
        pass
    elif item == "3":
        pass
    elif item == "4":
        pass
    elif item == "5":
        print("Exiting the program. All changes have been made. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice, Please try 1-5")


if __name__ == "__main__":
    main()