#Comp Bio Fall 2018
#Assignment 2, Question 4
#SBU ID : 112027432

#Defining Variables
Trie = [[-1,-1,-1,-1]]
maxNode = 1
currentNode = 0
dnaString = ""

def leaf(Node):
	for i in Trie[Node]:
		if i != -1:
			return False
	return True

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

def prefixTrieMatching(dnaString,Trie):
	currentNode = 0
	currentNucleotide = 0

	while True:
		#If Leaf Node, means some pattern is Prefix of Text
	 	if leaf(currentNode):
	 		#print(currentNode)
	 		return True
	 	else:
	 		#If -1, means no path forward
	 		if currentNucleotide == len(dnaString):
	 			return False
	 		elif Trie[currentNode][nucleotideIndex(dnaString[currentNucleotide])] == -1:
	 	 		return False
	 		else:
	 	 		currentNode = Trie[currentNode][nucleotideIndex(dnaString[currentNucleotide])]
	 	 		currentNucleotide += 1

i = 0
with open("rosalind_ba9b.txt","r") as PatternsFile:
	for Pattern in PatternsFile:
	
		Pattern = Pattern.strip()
		if i == 0:
			dnaString = Pattern
			i = 1
			continue

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

for i in range(0,len(dnaString)):
	#If Found in substring of Text, print the index
	if prefixTrieMatching(dnaString[i:],Trie):
		print(i,"",end="")
