#Hungry Fox

def reconstructStr(string, rChar):
	updatedStr = ''
	for char in string:
		if char != rChar:
			updatedStr+=char

	print(updatedStr, " char - ", rChar)
	return updatedStr


def checkAnagram(str1, str2):
	string1 = str1
	string2 = str2
	for charStr1 in range(len(str1)):
		for charStr2 in range(len(str2)):
			if(str1[charStr1] == str2[charStr2]):
				string1 = reconstructStr(string1, str1[charStr1])
				string2 = reconstructStr(string2, str2[charStr2])
	return string1


str1 = input("Enter a string ")
str2 = input("Input a string ")
checkAnagram(str1, str2)