#Comp Bio Fall 2018
#Assignment 2, Question 4
#SBU ID : 112027432

#Defining Variables
Trie = [[-1,-1,-1,-1]]
maxNode = 1
currentNode = 0

def nucleotideIndex(nucleotide):
	if nucleotide == 'A':
		return 0
	elif nucleotide == 'C':
		return 1
	elif nucleotide == 'G':
		return 2
	elif nucleotide == 'T':
		return 3

def indexNucleotide(index):
	if index == 0:
		return 'A'
	elif index == 1:
		return 'C'
	elif index == 2:
		return 'G'
	elif index == 3:
		return 'T'

with open("rosalind_ba9a.txt","r") as PatternsFile:
	for Pattern in PatternsFile:
		
		Pattern = Pattern.strip()
		currentNode = 0

		for i in Pattern:
			#If there is no corresponding edge, make new node
			if Trie[currentNode][nucleotideIndex(i)] == -1:
				Trie.append([-1,-1,-1,-1])
				Trie[currentNode][nucleotideIndex(i)] = maxNode
				currentNode = maxNode
				maxNode += 1
			else:
				currentNode = Trie[currentNode][nucleotideIndex(i)]

for i in range(0,len(Trie)):
	for j in range(0,len(Trie[i])):
		if Trie[i][j]!=-1:
			print(i,"->",Trie[i][j],":",indexNucleotide(j),sep="")