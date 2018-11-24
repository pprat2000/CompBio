#Comp Bio Fall 2018
#Assignment 1, Question 7
#SBU ID : 112027432

#Taking inputs
dnaFile = open("rosalind_ba6e.txt","r")
k = int(dnaFile.readline())
dnaString1 = dnaFile.readline()
dnaString2 = dnaFile.readline()

#Dictionary to store position of kmer occurences
kmerPosition = {}
#Dictionary used generate complement
nucleotideComplement = {'A':'T','C':'G','G':'C','T':'A'}

#Function to generate a reverse complement
def reverseComplement(kmer):
	complementkmer = ""
	for i in kmer:
		complementkmer += nucleotideComplement[i]
	return complementkmer[::-1]

#Update the kmerPosition dictionary
for i in range(0,len(dnaString2) - k + 1):
	kmer = dnaString2[i:i+k]
	complementkmer = reverseComplement(kmer)
	
	if kmer in kmerPosition:
		kmerPosition[kmer].append(i)
	else:
		kmerPosition[kmer] = [i]

	if complementkmer in kmerPosition:
		kmerPosition[complementkmer].append(i)
	else:
		kmerPosition[complementkmer] = [i]

#Now we know the position of all kmers in second string
#Just parse the first string and if match, print combination
for i in range(0,len(dnaString1) - k + 1):
	kmer = dnaString1[i:i+k]

	if kmer in kmerPosition:
		for j in kmerPosition[kmer]:
			print("(",i,", ",j,")",sep="")