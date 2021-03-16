import sqlite3

connection = sqlite3.connect("Customers.db")  # The .db extension is optional
cursor = connection.cursor()  # Executes SQL queries

# Alternative DB created only in memory
# mem_conn = sqlite3.connect(":memory:")
# cursor = mem_conn.cursor()

# Create the table to hold entries
cursor.execute("""
CREATE TABLE Customers
	(id INTEGER PRIMARY KEY,
	LName TEXT,
