def float_check(num):
	try:
		float(num)
	except ValueError:
		print("Not a float number.")
