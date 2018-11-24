#Comp Bio Fall 2018
#Assignment 2, Question 6
#SBU ID : 112027432

#Defining Variables
SuffixLocation = {}

SuffixFile = open("rosalind_ba9g.txt")
Text = SuffixFile.readline()
SuffixFile.close()
Text=Text.strip()
Text = Text[:-1]

for i in range(0,len(Text)):
	SuffixLocation[Text[i:]] = i
#For the Dollar
print(len(Text),end="")

for key in sorted(SuffixLocation.keys()):
	print(",",SuffixLocation[key],end="")