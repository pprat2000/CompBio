#Comp Bio Fall 2018
#Assignment 3, Question 4
#SBU ID : 112027432
#Python 3.6

i = 0
word1 = ""
word2 = ""
BLOSUM62 = dict()
gapStart = -11
gapExtend = -1

scoringFile = open("BLOSUM62.txt",'r')
row  = scoringFile.readline().strip().split(" ")
row = [x for x in row if x != '']
for line in scoringFile:
	line = line.strip().split(" ")
	line = [x for x in line if x != '']
	x = line[0]
	for i in range(1,len(line)):
		BLOSUM62[(row[i-1],x)] = int(line[i])
scoringFile.close()

i=0
with open("rosalind_gaff.txt",'r') as stringFile:
	for line in stringFile:
		if line[0] == '>':
			i += 1
			continue
		if i == 1:
			word1 += line.strip()
		if i == 2:
			word2 += line.strip()
stringFile.close()

n = len(word1)
m = len(word2)

M = [[0 for i in range(m+1)] for i in range(n+1)]
X = [[0 for i in range(m+1)] for i in range(n+1)]
Y = [[0 for i in range(m+1)] for i in range(n+1)]
bpM = [[0 for i in range(m+1)] for i in range(n+1)]
bpX = [[0 for i in range(m+1)] for i in range(n+1)]
bpY = [[0 for i in range(m+1)] for i in range(n+1)]

for i in range(1,m+1):
	M[0][i] = float('-inf')
	X[0][i] = gapStart + (i-1)*gapExtend
	bpX[0][i] = 2
	Y[0][i] = float('-inf')

for i in range(1,n+1):
	M[i][0] = float('-inf')
	X[i][0] = float('-inf')
	Y[i][0] = gapStart + (i-1)*gapExtend
	bpY[i][0] = 3

for i in range(1,n+1):
	for j in range(1,m+1):
		l = [M[i-1][j-1],X[i-1][j-1],Y[i-1][j-1]]
		M[i][j] = BLOSUM62[word1[i-1],word2[j-1]] + max(l)
		bpM[i][j] = l.index(max(l))+1
		
		l = [gapStart+M[i][j-1],gapExtend+X[i][j-1],gapStart+Y[i][j-1]]
		X[i][j] = max(l)
		bpX[i][j] = l.index(max(l))+1

		l = [gapStart+M[i-1][j],gapStart+X[i-1][j],gapExtend+Y[i-1][j]]
		Y[i][j] = max(l)
		bpY[i][j] = l.index(max(l))+1

# print(M,"\n")
# print(X,"\n")
# print(Y,"\n")
l = [M[n][m],X[n][m],Y[n][m]]
print(max(l))

idx = l.index(max(l))
i,j = n,m
L = [bpM,bpX,bpY]
Alignment = ["",""]

while L[idx][i][j] != 0:
	nextIdx = L[idx][i][j] - 1
	print(i,j)
	if idx == 0:
		Alignment[0] = word1[i-1] + Alignment[0]
		Alignment[1] = word2[j-1] + Alignment[1]
		i -=1
		j -= 1
	elif idx == 1:
		Alignment[0] = "-" + Alignment[0]
		Alignment[1] = word2[j-1] + Alignment[1]
		j -= 1
	elif idx == 2:
		Alignment[0] = word1[i-1] + Alignment[0]
		Alignment[1] = "-" + Alignment[1]
		i -= 1
	idx = nextIdx

print(Alignment[0])
print(Alignment[1])
	