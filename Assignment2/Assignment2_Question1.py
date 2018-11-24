#Comp Bio Fall 2018
#Assignment 2, Question 1
#SBU ID : 112027432

#Defining Variables
S = set()
#Dictionary used generate complement
nucleotideComplement = {'A':'T','C':'G','G':'C','T':'A'}

#Function to generate a reverse complement
def reverseComplement(kmer):
	complementkmer = ""
	for i in kmer:
		complementkmer += nucleotideComplement[i]
	return complementkmer[::-1]


#Taking inputs
with open("rosalind_dbru.txt","r") as KmerFile:
	for kmer in KmerFile:
		S.add(kmer.strip())
		S.add(reverseComplement(kmer.strip()))

KmerFile.close()

for kmer in S:
	print("(",kmer[:-1],", ",kmer[1:],")",sep="")

