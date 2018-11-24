#Comp Bio Fall 2018
#Assignment 1, Question 3
#SBU ID : 112027432

#Global Variables
#Question asks for a 4-mer composition
k = 4

#Different nucleotides
Nucleotide = "ACGT"

#Creating a Dictionary for storing k-mer composition
kMerComp = {}

kmer="AAAA"

#This is needed. Otherwise kmer with count 0 will be missed in output
def GenerateAllkMers(kmer,length):
	if length == k:
		kMerComp[kmer] = 0
		return
	else:
		for i in Nucleotide:
			kmer = kmer[:length] + i + kmer[length+1:]
			GenerateAllkMers(kmer,length+1)
		return

#Taking input
dnaString = ""
tempString = ""

#Taking inputs
with open("rosalind_kmer.txt", "r") as dnaFile:
    for line in dnaFile:
    	if line.find('>') == -1:
    		dnaString = dnaString + line.rstrip()

#print(dnaString)
#Generating all kmers and populating the Dictionary
GenerateAllkMers(kmer,0)

#Iterate over the DNA String, Sliding window
for i in range(0 , len(dnaString) - k + 1):
	#Splicing out the current kmer
	#and incrementing the count
	kmer = dnaString[i:i+k]
	kMerComp[kmer] += 1

#Printing the kmer Composition	
for kmer in sorted(kMerComp.keys()):
	print(kMerComp[kmer],"",end="")