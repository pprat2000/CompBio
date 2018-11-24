#Comp Bio Fall 2018
#Assignment 1, Question 1
#SBU ID : 112027432

#Taking input
dnaString = input()

#Creating a dictionary
nucleotideCount = {"A":0, "C":0, "G":0, "T":0}

#Counting the nucleotides
for nucleotide in dnaString:
	nucleotideCount[nucleotide] += 1

#Printing the Count
for nucleotide in sorted(nucleotideCount.keys()):
	print(nucleotideCount[nucleotide], " ")
