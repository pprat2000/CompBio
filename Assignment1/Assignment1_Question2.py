#Comp Bio Fall 2018
#Assignment 1, Question 2
#SBU ID : 112027432

#Taking input
dnaString = input()

rnaString = ""
#Counting the nucleotides
for nucleotide in dnaString:
	if nucleotide == 'T':
		rnaString = rnaString + 'U'
	else:
		rnaString = rnaString + nucleotide

print(rnaString)