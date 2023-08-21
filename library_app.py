from library_db import LibraryCRUD

class LibraryApp:
    def __init__(self):
        self.library_db = LibraryCRUD()

    def present_menu(self):
        print("\nWelcome to the Library. What do you intent?\n")
        print("1 - show all books")
        print("2 - Add a new book with basic information")
        print("2 - Add a new book with complete information")
        print("3 - Reenter information for an existing book")
        print("4 - Delete a book by id")
        print("5 - Search for a book")
        print("6 - Exit")
        choice = input("Type the desirable number: ")
        self.library_db.execute_action(choice)

#
# Main
if __name__ == "__main__":
    try:
        library_app = LibraryApp()
        while (True):
            library_app.present_menu()
    except Exception as e:
        print("error: ", str(e))
