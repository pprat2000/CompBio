#Comp Bio Fall 2018
#Assignment 1, Question 3
#SBU ID : 112027432
 
pattern = input()
 
dnaString = input()
 
length = len(pattern)
 
startIndex = []
 
for i in range(0,len(dnaString) - length + 1):
	temp = dnaString[i:i+length]
	if pattern == temp:
		startIndex.append(i)
 
 
for i in startIndex:
	print(i,"",end="")