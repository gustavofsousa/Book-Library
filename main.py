import mysql.connector

class LibraryCRUD:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "gusta",
            password = "123456",
            database = "db_gjbp"
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def __del__(self):
        self.cursor.close()
        self.connection.close()












# Main
if __name__ == "__main__":
    libraryGJBP = LibraryCRUD();
    print("I create then delete the library")
