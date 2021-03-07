cursor.execute("SELECT * FROM Tools")
for row in cursor:
	print ("-" * 10)
	print ("ID:", row[0])
	print ("Name:", row[1])
	print ("Size:", row[2])
	print ("Price:", row[3])
	print ("-" * 10)
