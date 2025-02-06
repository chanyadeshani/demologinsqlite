import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_file="coffee_brew.db"):
        try:
            self.connection = sqlite3.connect(db_file, check_same_thread=False)
            self.cursor = self.connection.cursor()
            print("Database connection established.")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_user_tbl(self):
        # SQL command to create a table in the database
        sql_command = """CREATE TABLE IF NOT EXISTS users ( 
        user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username VARCHAR(20), 
        password VARCHAR(30));"""

        # Execute the statement
        self.cursor.execute(sql_command)

    def add_user_data(self, username, password):
        # SQL command to insert data into the table
        sql_command = """INSERT INTO users (username,password)  
                             VALUES (?, ?);"""

        # Execute the insert statement with the provided values
        self.cursor.execute(sql_command, (username, password))

        # Commit changes to the database
        self.connection.commit()

    def get_userdata(self, username):
        """
        Lists all orders from the database.
        """
        list_sql = "SELECT * FROM `users` WHERE username = ?;"

        try:
            self.cursor.execute(list_sql, (username,))
            records = self.cursor.fetchall()
            return records
        except Error as e:
            print(f"Error retrieving user data: {e}")
            return []

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
