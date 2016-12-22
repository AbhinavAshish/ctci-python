''' Question Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?'''
#x=raw_input("Enter the String ")


#Solution in n square (not preferred )
# Approach Take one character and match it with the other characters. Note the solution makes sure that the lowercase and uppercase characters are the same
def uniqueCharacters(inputString) :
	for index in range(0,len(inputString)):
		for index2 in range(index+1,len(inputString)):
			if (inputString[index].lower() == inputString[index2].lower()):
				return False
	return True

#solution in nlogn (not preffered)
#Approach : Arrange the characters in ascending order and check for your neighbour 
def uniqueCharactersSorted(inputString) :
	c = "".join(sorted(inputString))
	for index in range(0,len(inputString)-1):
		if(c[index].lower()==c[index+1].lower()):
			return False
	return True		

#solution in n preffered
#Approach : Arrange the characters in ascending order and check for your neighbour 

def uniqueCharactersPreffered(inputString): 
	char_set = [0]*256 
	for chars in inputString:
		if(char_set[ord(chars)]==1): 
			return False
		else :
			char_set[ord(chars)]=1

	return True			

#inputString = "Abhinav"
inputString= raw_input("Enter the String :")
print uniqueCharactersPreffered(inputString)

