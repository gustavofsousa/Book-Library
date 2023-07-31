import mysql.connector

class LibraryCRUD:
    def __enter__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "servus",
            password = "newstory",
            database = "library_GJBP_db"
        )
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







# Main
if __name__ == "__main__":
    try:
        with LibraryCRUD() as library:
            print("Library created with success")
    except Except as e:
        print("error: ", str(e))
