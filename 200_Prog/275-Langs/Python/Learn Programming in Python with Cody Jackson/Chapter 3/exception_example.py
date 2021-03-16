num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
try:
	num1 = float(num1)
	num2 = float(num2)
	result = num1/num2
except ValueError:
	print ("Two numbers are required.")
except ZeroDivisionError:
	print ("Zero can't be a denominator.")
else:
	print ("{num1}/{num2}={result}".format(num1=num1, num2=num2, result=result))
