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

# Main
if __name__ == "__main__":
    try:
        with LibraryCRUD() as library:
            print("Library created with success")
            library.show_all_books() 
            library.add_book("The hobbit", "JRR Tolkien")
            library.show_all_books() 
    except Exception as e:
        print("error: ", str(e))
