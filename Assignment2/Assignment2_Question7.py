#Comp Bio Fall 2018
#Assignment 2, Question 7
#SBU ID : 112027432

#Defining Variables
SuffixLocation = {}
Patterns = []
i = 0
SuffixArray = []
length = 0
Text = ''

def LinearSearch(l,r,Pattern):
	l = len(Pattern)
	
	for i in range(l,r+1):
		if SuffixArray[i] + l < len(Text):
			if Pattern == Text[SuffixArray[i]:SuffixArray[i]+l]:
				print(SuffixArray[i],"",end="")

def BinSearch(l,r,Pattern):
	if l < r:
		mid = int((l+r)/2)

		if Text[SuffixArray[mid]] > Pattern[0]:
			BinSearch(l,mid-1,Pattern)
		elif Text[SuffixArray[mid]] < Pattern[0]:
			BinSearch(mid+1,r,Pattern)
		else:
			LinearSearch(l,r,Pattern)

with open("rosalind_ba9h.txt","r") as PatternsFile:
	for Pattern in PatternsFile:
	
		Pattern = Pattern.strip()
		if i == 0:
			Text = Pattern
			i = 1
			continue
		Patterns.append(Pattern)

for i in range(0,len(Text)):
	SuffixLocation[Text[i:]] = i
SuffixLocation['$'] = len(SuffixLocation)

for key in sorted(SuffixLocation.keys()):
	SuffixArray.append(SuffixLocation[key])
del SuffixLocation

#Use binary Search
# for Pattern in Patterns:
# 	l = len(Pattern)
# 	for key,value in SuffixLocation.items():
# 		if len(key) < l:
# 			continue
# 		elif Pattern == key[:l]:
# 			print(value,"",end="")

# for Pattern in Patterns:
# 	l = len(Pattern)
# 	for index in SuffixArray:
# 		if index + l < len(Text):
# 			if Pattern == Text[index:index+l]:
# 				print(index,"",end="")

for Pattern in Patterns:
	BinSearch(0,len(SuffixArray)-1,Pattern)