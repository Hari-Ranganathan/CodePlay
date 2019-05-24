print("Python Calculator:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
option = input("What are we calculating today? (1, 2, 3, or 4) ")
option = int(option)
if option in [1, 2, 3, 4]:
	number1 = input("Enter the first number: ")
	number2 = input("Enter the second number: ")
	if(number1 != "" and number2 != ""):
		number1 = int(number1)
		number2 = int(number2)
		if option == 1:
			number3 = number1 + number2
		elif option == 2:
			number3 = number1 - number2
		elif option == 3:
			number3 = number1 * number2
		elif option == 4:
			number3 = number1 / number2
		print(number1," + ",number2 ," = ",number3)
	else:
		print("Given input is not valid number");
else:
	print("Please select any of the given option (1, 2, 3, 4)")