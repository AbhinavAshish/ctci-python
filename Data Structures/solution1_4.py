#Write a method to replace all spaces in a string with '%20'. You may assume that the
#string has sufficient space at the end of the string to hold the additional characters,
#and that you are given the "true" length of the string. (Note: if implementing in Java,
#please use a character array so that you can perform this operation in place.)

# general approach is to start from behind and then fill the spaces by calculating new length but in python 
# we can actually do it pretty easily as it allows breaking into list

def replaceSpaces(string1) :
	list1 = list(string1)
	for index in range(0,len(string1)):
		if (list1[index]==' '):
			list1[index]= "%20"
	string1 = "".join(list1)		
	print string1		

#putting another approach which you have to take in languages like Java where you have character arrays
def replaceSpacesJavalogic(string1) :
	list1 = list(string1)
	counter =0
	for index in range(0,len(string1)):
		if (list1[index]==' '):
			counter += 1 
	newlength = len(string1) + counter * 2
	
	for index in range(len(string1),newlength):
		list1.insert(index,'k')


	for index in range(len(string1)-1,-1,-1):
		#print newlength	
		if (list1[index]==' ') :
			list1[newlength-1] = '0' 
			list1[newlength-2] = '2'
			list1[newlength-3] = '%'
			newlength-=3
		else :
			list1[newlength-1] = list1[index]
			newlength-=1

	string1 = "".join(list1)		
	print string1							


string1 = input("Enter the String")
replaceSpaces(string1)
replaceSpacesJavalogic(string1)

