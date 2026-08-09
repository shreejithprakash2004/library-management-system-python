import datetime


class LMS:

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}

        book_id = 101

        with open(self.list_of_books, "r") as file:
            books = file.readlines()

        for book in books:
            self.books_dict[book_id] = {
                "Book Name": book.strip(),
                "Lender Name": "",
                "Issue Date": "",
                "Due Date": "",
                "Return Date": "",
                "Fine": 0,
                "Status": "Available"
            }

            book_id += 1

    # Display Books Module

    def display_books(self):
        print("\n---------------- LIST OF BOOKS ----------------")
        print(f"Books available in {self.library_name}")
        print("------------------------------------------------")

        for book_id, details in self.books_dict.items():
            print(
                f"{book_id:<5} "
                f"{details['Book Name']:<35} "
                f"[{details['Status']}]"
            )

    # Issue Book Module

    def issue_book(self):

        try:
            book_id = int(input("Enter Book ID : "))
        except ValueError:
            print("Please enter a valid Book ID.")
            return

        if book_id not in self.books_dict:
            print("Book ID not found.")
            return

        if self.books_dict[book_id]["Status"] == "Issued":
            print(
                f"\nBook already issued to "
                f"{self.books_dict[book_id]['Lender Name']}"
            )
            return

        lender_name = input("Enter your name : ").strip()

        if lender_name == "":
            print("Name cannot be empty.")
            return

        # Current date and time
        issue_date = datetime.datetime.now()

        # Due date after 14 days
        due_date = issue_date + datetime.timedelta(days=14)

        self.books_dict[book_id]["Lender Name"] = lender_name
        self.books_dict[book_id]["Issue Date"] = issue_date.strftime(
            "%d-%m-%Y %H:%M:%S"
        )
        self.books_dict[book_id]["Due Date"] = due_date.strftime(
            "%d-%m-%Y %H:%M:%S"
        )
        self.books_dict[book_id]["Return Date"] = ""
        self.books_dict[book_id]["Fine"] = 0
        self.books_dict[book_id]["Status"] = "Issued"

        print("\nBook Issued Successfully.")
        print(f"Issued To  : {lender_name}")
        print(
            f"Issue Date : "
            f"{self.books_dict[book_id]['Issue Date']}"
        )
        print(
            f"Due Date   : "
            f"{self.books_dict[book_id]['Due Date']}"
        )

    # Add Book Module

    def add_book(self):

        new_book = input("Enter Book Name : ").strip()

        if new_book == "":
            print("Book name cannot be empty.")
            return

        if len(new_book) > 30:
            print("Book name is too long.")
            return

        # Check duplicate book
        for details in self.books_dict.values():
            if details["Book Name"].lower() == new_book.lower():
                print("Book already exists.")
                return

        new_id = max(self.books_dict) + 1

        self.books_dict[new_id] = {
            "Book Name": new_book,
            "Lender Name": "",
            "Issue Date": "",
            "Due Date": "",
            "Return Date": "",
            "Fine": 0,
            "Status": "Available"
        }

        with open(self.list_of_books, "a") as file:
            file.write(new_book + "\n")

        print(f"{new_book} added successfully.")
        print(f"New Book ID: {new_id}")

    # Return Book Module

    def return_book(self):

        try:
            book_id = int(input("Enter Book ID : "))
        except ValueError:
            print("Please enter a valid Book ID.")
            return

        if book_id not in self.books_dict:
            print("Book ID not found.")
            return

        if self.books_dict[book_id]["Status"] == "Available":
            print("Book is already available.")
            return

        # Current return date and time
        return_date = datetime.datetime.now()

        # Get the stored due date
        due_date = datetime.datetime.strptime(
            self.books_dict[book_id]["Due Date"],
            "%d-%m-%Y %H:%M:%S"
        )

        # Calculate late days
        if return_date > due_date:
            late_days = (return_date.date() - due_date.date()).days
        else:
            late_days = 0

        # ₹5 fine per late day
        fine = late_days * 5

        self.books_dict[book_id]["Return Date"] = return_date.strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        self.books_dict[book_id]["Fine"] = fine

        self.books_dict[book_id]["Lender Name"] = ""
        self.books_dict[book_id]["Issue Date"] = ""
        self.books_dict[book_id]["Due Date"] = ""
        self.books_dict[book_id]["Status"] = "Available"

        print("\nBook Returned Successfully.")
        print(f"Return Date : {return_date.strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"Late Days   : {late_days}")
        print(f"Fine        : ₹{fine}")


# Create Library

library = LMS("list_of_books.txt", "Python Library")


# Menu

menu = {
    "D": "Display Books",
    "I": "Issue Book",
    "A": "Add Book",
    "R": "Return Book",
    "Q": "Quit"
}


while True:

    print("\n========== WELCOME TO PYTHON LIBRARY MANAGEMENT SYSTEM ==========")

    for key, value in menu.items():
        print(f"{key} - {value}")

    choice = input("\nEnter Choice : ").upper()

    if choice == "D":
        print("\nDisplaying Books...")
        library.display_books()

    elif choice == "I":
        print("\nIssuing Book Section...")
        library.issue_book()

    elif choice == "A":
        print("\nAdding Book Section...")
        library.add_book()

    elif choice == "R":
        print("\nReturning Book Section...")
        library.return_book()

    elif choice == "Q":
        print("\nThank You!")
        break

    else:
        print("Invalid Choice.")