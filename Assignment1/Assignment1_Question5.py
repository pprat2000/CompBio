#Comp Bio Fall 2018
#Assignment 1, Question 5
#SBU ID : 112027432

#Global Variables
#Creating a Dictionary for storing each k-mer Count
kMerComp = {}
Nucleotide = "ACGT"
kmer=""
maxCount = -1

#Taking input
dnaString = input()
k = int(input())

#Iterate over the DNA String, Sliding window
for i in range(0 , len(dnaString) - k + 1):
	#Splicing out the current kmer
	#and incrementing the count
	kmer = dnaString[i:i+k]
	if kmer in kMerComp:
		kMerComp[kmer] += 1
	else:
		kMerComp[kmer] = 1


#Finding max value 
for kmer in kMerComp.keys():
	if(kMerComp[kmer] > maxCount):
		maxCount = kMerComp[kmer]

#Printing all kmer corresponding to max value
for kmer in sorted(kMerComp.keys()):
	if(kMerComp[kmer] == maxCount):
		print(kmer,"",end="")