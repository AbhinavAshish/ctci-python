

#Implement a function which reverses a string 

#Approach use a temporary variable and replace. Solution in n
def reverseString (inputStr) :
	inputString= list(inputStr)
	for index in range(0,len(inputString)/2):
		temp = inputString[index]
		inputString[index]= inputString[len(inputString)-1-index]
		inputString[len(inputString)-1-index] = temp

	inputStr ="".join(inputString)
	print inputStr	
	return

#inputString = ""
inputString= raw_input("Enter the String :")
reverseString(inputString)
