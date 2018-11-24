#Comp Bio Fall 2018
#Assignment 1, Question 7
#SBU ID : 112027432

#Defining Variables
CodonToProteinMap = {}
dnaString = ""
introns = []
i = 0
rnaString = ""
Protein = ""
temp = ""
#Filling Inverse Table(Codon Protein Mapping)
with open("file.txt","r") as inverseTableFile:
	for line in inverseTableFile:
		if i == 0:
			key = line.rstrip()
			i = 1
		else:
			value = line.rstrip()
			i = 0
			CodonToProteinMap[key] = value

i = -1
#Taking inputs
with open("rosalind_splc.txt", "r") as dnaFile:
    for line in dnaFile:
    	if line.find('>') != -1:
    		i += 1
    	else:
    		if i == 0:
    			dnaString = dnaString + line.rstrip()
    		else:
    			introns.append(line.rstrip())
#Removing introns
for intron in introns:
	intronPosition = dnaString.find(intron)
	if intronPosition != -1:
		dnaString = dnaString[:intronPosition] + dnaString[intronPosition + len(intron):]

#Transcribing DNA to RNA
for nucleotide in dnaString:
	if nucleotide == 'T':
		rnaString = rnaString + 'U'
	else:
		rnaString = rnaString + nucleotide

#Translating RNA to Protein using Inverse Table
i = 3
for j in range(0,int(len(rnaString)/3)):
	Codon = rnaString[(i*j) : (i*j)+i]
	temp = CodonToProteinMap[Codon]
	if temp == ".":
		break
	Protein += temp

print(Protein)