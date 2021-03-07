smith_id = customer_insert("Smith", "John", "312 Hard St.", "Somewhere", "NY")
smith_order1 = order_insert("Shoes", 23.99, 3490, smith_id)
smith_order2 = order_insert("Shoes", 65.00, 5512, smith_id)

connection.commit()  # Write data to database
cursor.close()  # Close database
