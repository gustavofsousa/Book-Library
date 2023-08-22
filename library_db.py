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
                self.add_simple_book()
            elif choice == "3":
                self.add_complete_book()
            elif choice == "4":
                self.update_book()
            elif choice == "5":
                self.delete_book()
                self.update_id_seqence()
            elif choice == "6":
                self.search_book()
            elif choice == "7":
                exit()
    
# COMMANDS OF LIBRARY
    def show_all_books(self):
        self.cursor.execute("select * from livros")
        all_books = self.cursor.fetchall()
        print()
        for books in all_books:
            print(books)

    def add_simple_book(self):
        title = input("Type the books's title: ")
        author = input("Type the books's author: ")

        command = "insert into livros (title, author) values (?, ?)"
        self.cursor.execute(command, (title, author))
        self.connection.commit()

    def add_complete_book(self):
        title = input("Type the books's title: ")
        author = input("Type the books's author: ")
        pages = input("Type the books's page: ")
        tag = input("Type the books's tag(theme): ")
        sinopse = input("Type the books's sinopse: ")

        command = "insert into livros (title, author, pages, tag, sinopse) values (?, ?, ?, ?, ?)"
        self.cursor.execute(command, (title, author, pages, tag, sinopse))
        self.connection.commit()

    def update_book(self):
        book_id = input("Type the number's book: ")
        title = input("Type the books's title: ")
        author = input("Type the books's author: ")
        pages = input("Type the books's page: ")
        tag = input("Type the books's tag(theme): ")
        sinopse = input("Type the books's sinopse: ")

        command = "UPDATE livros SET title = ?, author = ?, pages = ?, tag = ?, sinopse = ? WHERE id = ?"
        self.cursor.execute(command, (title, author, pages, tag, sinopse, book_id))
        self.connection.commit()

    def delete_book(self):
        id_delete = input("Type the number's book you want to delete: ")
        command = "delete from livros where id = ?"
        self.cursor.execute(command, (id_delete,))
        self.connection.commit()

    def update_id_seqence(self):
        self.cursor.execute("SELECT id FROM livros ORDER BY id")
        rows = self.cursor.fetchall()
    
        current_id = 1
        for row in rows:
            if row[0] != current_id:
                self.cursor.execute("UPDATE livros SET id = ? WHERE id = ?", (current_id, row[0]))
                self.connection.commit()
            current_id += 1

    def search_book(self):
        book_name = input("Type the book's title to search in database: ")
        search_term = '%' + book_name.lower() + '%'

        command = "select * from livros where lower(title) like ?"
        self.cursor.execute(command,(search_term,))
        search_results = self.cursor.fetchall()

        if (search_results):
            print("\nResults found:")
            for book in search_results:
                print(book)
        else:
            print("\nNo matching books found.")
