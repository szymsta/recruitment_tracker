# Recruitment Tracker

**Recruitment Tracker**  is a Python script that helps you manage and track job applications. This tool allows you to easily add, remove, update and display job offers you have applied for, along with key details such as url, position, company name, salary range, and application date. It helps streamline the process of keeping track of your job applications in one central place.

---

## Features

- **Add Job Offers**: Easily add new job offers to your tracker by providing the URL, position, company name, salary range, and application date.
- **View Job Offers**: View all the job offers you’ve applied for in a formatted table that clearly displays the important details.
- **Remove Job Offers**: Quickly remove any job offer from your list if the application is no longer relevant.
- **Update Job Offers**: Modify the details of previously saved job offers, such as position, company, and salary.
- **Persistent Storage**: All data is saved in a JSON file (`offers.json`), ensuring that your job offers are preserved across multiple sessions.
- **Input Validation**: The script validates user inputs for URL format, application date, and salary to ensure data integrity.

---

## Requirements

Before running the script, ensure you have the following installed:

- **Python 3.7+**: You can download the latest version of Python from the [official Python website](https://www.python.org/downloads/).
- **Required Python Libraries**:
  - `tabulate`: For formatting job offers into a neat table. Install it by running:
    ```bash
    pip install tabulate
    ```

---

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/szymsta/recruitment_tracker.git
    ```

2. **Install Dependencies**:
    Install the required libraries using `pip`:
    ```bash
    pip install tabulate
    ```

3. **Check `offers.json` File**:
    Ensure the `offers.json` file is present in the same directory as the script. If it doesn’t exist, the script will automatically create it the first time you run it.

---

## Usage

Once you’ve installed the dependencies and verified the required files, you can run the script.

To start the script, open your terminal or command prompt and execute:

```bash
python recruitment_tracker.py
```
The script will present a menu with options, allowing you to interact with the program.

---

## Menu

This menu allows you to choose one of the available actions by entering the corresponding number. The options are as follows:

```bash
==============================
Recruitment tracker
==============================

Press number to choose what you want to do:
    1. Add an offer I applied for
    2. Remove an offer I applied for
    3. Update an offer I applied for
    4. Show all offers I applied for
    5. Exit program
Enter your choice (1-5): 
```

---

## Example of Use

For example, after selecting 1, enter the details of the job offer you are applying for:

```bash
Enter the details for the offer you applied for:
URL for the offer: https://www.example.com/job/bigdata-engineer
Position I applied for: Big Data Engineer
Company name: Example Inc.
Application date (YYYY-MM-DD): 2025-05-05
Minimum salary (only numbers): 10
Maximum salary (only numbers): 20
```
After adding some job offers, you can view them all by selecting option 4 (Show all offers). The offers will be displayed in a neatly formatted table:

```bash
+---+-------------------+--------------+-------------------------------------------+-------------------+------------+------------+
| # | Position          | Company      | Link                                      | Application Date  | Salary Min | Salary Max |
+---+-------------------+--------------+-------------------------------------------+-------------------+------------+------------+
| 1 | Big Data Engineer | Example Inc. | https://www.example.com/job/bigdata-engineer | 2025-05-05      | 10      | 20      |
+---+-------------------+--------------+-------------------------------------------+-------------------+------------+------------+
```

---

## Additional Features and Functionality

- Validation - The script ensures that the data entered for the offer is valid:

  - URL Validation: The URL must be in the proper format (e.g., https://www.example.com).
  - Date Validation: The application date must be in the YYYY-MM-DD format.
  - Salary Validation: Both the minimum and maximum salaries must be positive integers.
- Error Handling: The script gracefully handles any errors, such as invalid input or file access issues, and provides meaningful feedback to guide users through the process.

---
## File Structure

Here's a breakdown of the project files:

```bash
/recruitment_tracker
    ├── offers.json             # Stores the job offer data.
    ├── recruitment_tracker.py  # Main Python script for the Recruitment Tracker.
    ├── requirements.txt        # List of dependencies (for easy installation).
    ├── config.py               # Configuration file containing constants used throughout the project.
    ├── validator/              # Directory containing the Validator class for input validation.
    │   └── validator.py        # Contains validation methods for URL, date, and salary inputs.
    ├── offer_manager/          # Directory for managing offers
    │   └── offer_controller.py # Manages add/show/update/remove operations.
    │   └── input_handler.py    # Collects user input for offers.
    ├── file_manager/           # Directory for file manager
    │   └── file_manager.py     # Manages file reading and writing for offers.
    └── README.md               # Project documentation, describing the project and setup instructions.
```
