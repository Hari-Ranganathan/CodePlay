#Rounding of the value without using the round()function 
import math
def customRound(x):
	print("Value i have received ",math.ceil(x))
	print("Value after the initial calculation",math.ceil(x/10))
	return int(math.ceil(x/10))
print ("Built-in Round off function ::", round(10/11))
print ("Custom Round off function ::",customRound(10/11))

#it will not work under the scenario of when the value is goes below 5