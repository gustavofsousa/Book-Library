import sqlite3

class LibraryCRUD:
    def __enter__(self):
        self.connection = sqlite3.connect("your_library")
        self.cursor = self.connection.cursor()
        self.create_table()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.connection.close()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author varchar(45),
                pages INT,
                tag VARCHAR(45),
                sinopse varchar(255)
            )
        """)

    def add_book(self, title, author):
        command = "insert into livros (title, author) values (?, ?)"
        self.cursor.execute(command, (title, author))
        self.connection.commit()

    def show_all_books(self):
        self.cursor.execute("select * from livros")
        print(self.cursor.fetchall())

    def choose_action(self, choice):
        if choice == "1":
            self.show_all_books()
        elif choice == "2":
            self.add_book("name", "some writer")
        elif choice == "3":
            self.add_book("name", "some writer")
        # elif choice == "4":
        #     self.update_book("name", "some writer")
        # elif choice == "5":
        #     self.search_book("name", "some writer")
        elif choice == "6":
            exit()
 
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
        self.choose_action(choice)

# Main
if __name__ == "__main__":
    try:
        with LibraryCRUD() as library:
            while (True):
                library.present_menu()
    except Exception as e:
        print("error: ", str(e))
