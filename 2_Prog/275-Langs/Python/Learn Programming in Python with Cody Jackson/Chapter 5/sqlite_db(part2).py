	FName TEXT,
	Address TEXT,
	City TEXT,
	State TEXT)
""")

cursor.execute("""
CREATE TABLE Orders
	(id INTEGER PRIMARY KEY,
	Item_title TEXT,
	Price FLOAT,
	Order_Number INTEGER,
	customer_id INTEGER,
	FOREIGN KEY (customer_id) REFERENCES Customers(id))
""")
