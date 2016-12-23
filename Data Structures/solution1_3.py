#Given two strings, write a method to decide if one is a permutation of the other.

'''Approach 1 sort both the strings and compare . First check if the length is equal. If not we can just fail 
(Not preffered Complexity nlog n)'''

def permutationMatcher(string1 , string2) :
	
	if (len(string1)!=len(string2) ):
		return False
	else:
		list1= list (string1)
		list2 = list(string2)
		string1 = "".join(sorted(list1))
		string2 = "".join(sorted(list2))
		if (string1 == string2):
			return 	True
		else :
			return False


#Approach : build a list of with the count of each character and check if the next string has the same number.
# Questions to ask is this case sensitive . Does Blanks counts. The below solution allows blanks and does not take into account 
#lowercase 
def permutationMatcherPreffered(string1 , string2) :
	list1 = [0] *256
	if (len(string1)!=len(string2) ):
		return False
	else :	
		for index in range(0,len(string1)):
			list1[ord(string1[index])] = list1[ord(string1[index])] +1 

		for index in range(0,len(string2)):
			if (list1[ord(string2[index])]==0) :
				return False 
			else :
				list1[ord(string2[index])] = list1[ord(string2[index])] -1
		return True
				 
			
#string1 = "Antarctica is goofya"
#string2  = "Bntarctica is goofy"

string1= raw_input("Enter the first String :")
string2= raw_input("Enter the second String :")
print permutationMatcher(string1,string2)
print permutationMatcherPreffered(string1,string2)




