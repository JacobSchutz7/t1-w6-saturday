# Simple calculator using if-else statements

# Get user input
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+ - * /): ")
num2 = float(input("Enter second number: "))

# Perform calculation using if-else statements
if operation == '+':
	result = num1 + num2
elif operation == '-':
	result = num1 - num2
elif operation == '*':
	result = num1 * num2
elif operation == '/':
	if num2 != 0:
		result = num1 / num2
	else: 
		print("Error! Cannot devide by 0.")
else: 
	result = "Error! Invalid operation."

print(f"The result is {result}")