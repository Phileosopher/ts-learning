import sqlite3

connection = sqlite3.connect("Tools.db")
cursor = connection.cursor()

cursor.execute("SELECT name, size, price FROM Tools")
toolsTuple = cursor.fetchall()
for entry in toolsTuple:
    name, size, price = entry  # Unpack the tuples
    item = ("{}, {}, {}".format(name, size, price))
    print(item)
