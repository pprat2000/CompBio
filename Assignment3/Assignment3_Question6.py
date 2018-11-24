#Comp Bio Fall 2018
#Assignment 3, Question 6
#SBU ID : 112027432
#Python 3.6

def isHamming(s1,s2):
    c = 0
    for i in range(len(s1)):
    	if s1[i] != s2[i]:
    		c += 1
    if c > 4:
    	return False
    return True

i = 0
word1 = ""
word2 = ""
with open("rosalind_subo.txt",'r') as stringFile:
	for line in stringFile:
		if line[0] == '>':
			i += 1
			continue
		if i == 1:
			word1 += line.strip()
		if i == 2:
			word2 += line.strip()

print(word1)
print(word2)

r = "AGCAAAGGAAGCCTAGCAAAAACTCCTCGACA"
n = len(r)
c = 0

for i in range(len(word1)- n + 1):
	if isHamming(r,word1[i:i+n]):
		c += 1
print(c," ",sep="",end="")
c = 0
for i in range(len(word2) -n + 1):
	if isHamming(r,word2[i:i+n]):
		c += 1
print(c,sep="",end="")