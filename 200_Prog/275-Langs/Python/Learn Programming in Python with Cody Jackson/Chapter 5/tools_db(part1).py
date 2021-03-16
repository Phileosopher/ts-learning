import sqlite3

connection = sqlite3.connect("Tools.db")  # The .db extension is optional
cursor = connection.cursor()  # Executes SQL queries

# Create the table to hold entries
cursor.execute("""
CREATE TABLE Tools
(id INTEGER PRIMARY KEY,
name TEXT,
size TEXT,
price INTEGER)
""")
