def customer_insert(last_name, first_name, address, city, state):
	sql = "INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?)"
	cursor.execute(sql, (None, last_name, first_name, address, city, state))
	return cursor.lastrowid  # Get ID of object

def order_insert(item, price, order_num, customer_id):
	sql = "INSERT INTO Orders VALUES (?, ?, ?, ?, ?)"
	cursor.execute(sql, (None, item, price, order_num, customer_id))
	return cursor.lastrowid

johnson_id = customer_insert("Johnson", "Jack", "123 Easy St.", "Anywhere", "CA")
johnson_order1 = order_insert("Boots", 55.50, 4455, johnson_id)
johnson_order2 = order_insert("Shirt", 16.00, 4455, johnson_id)
johnson_order3 = order_insert("Pants", 33.00, 7690, johnson_id)
