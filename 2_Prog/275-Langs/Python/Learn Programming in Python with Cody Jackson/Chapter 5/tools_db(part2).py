# Populate table
for item in (
		(None, "Box Knife", "Small", 15),
		(None, "Drill", "Medium", 35),
		(None, "Axe", "Large", 55),
		(None, "Putty Knife", "Small", 25),
		(None, "Hammer", "Small", 25),
		(None, "Screwdriver", "Small", 10),
		(None, "Crowbar", "Large", 60),
		): 
	cursor.execute("INSERT INTO Tools VALUES (?, ?, ?, ?)", item)

connection.commit()  # Write data to database
cursor.close()  # Close database
