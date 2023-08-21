import sqlite3

class LibraryCRUD:
    def __enter__(self):
        self.connection = sqlite3.connect("your_library")
        self.cursor = self.connection.cursor()
        self.create_table()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

## SETTINGS OF LIBRARY
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author varchar(45),
                pages INT,
                tag VARCHAR(45),
                sinopse varchar(255)
            )
        """)

    
    def execute_action(self, choice):
        with self:
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
    
# COMMANDS OF LIBRARY
    def show_all_books(self):
        self.cursor.execute("select * from livros")
        all_books = self.cursor.fetchall()
        for books in all_books:
            print(books)

    def add_book(self, title, author):
        command = "insert into livros (title, author) values (?, ?)"
        self.cursor.execute(command, (title, author))
        self.connection.commit()

