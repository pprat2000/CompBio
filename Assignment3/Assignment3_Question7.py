#Comp Bio Fall 2018
#Assignment 3, Question 5
#SBU ID : 112027432
#Python 3.6


i = 0
word1 = ""
word2 = ""
BLOSUM62 = dict()
indelPenalty = -5

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
stringFile = open("rosalind_ba5k.txt",'r')
word1 = stringFile.readline().strip()
word2 = stringFile.readline().strip()
stringFile.close()

n = len(word1)
m = len(word2)

if m == 0:
    print(n)
if n == 0:
    print(m)


Grid = [[0 for i in range(n+1)] for i in range(m+1)]
BestWayToReach = [[0 for i in range(n+1)] for i in range(m+1)]

Grid[0][0] = 0
BestWayToReach[0][0] = -1

for i in range(1,n+1):
    BestWayToReach[0][i] = 0
    Grid[0][i] = Grid[0][i-1]+indelPenalty
        
for i in range(1,m+1):
    BestWayToReach[i][0] = 1
    Grid[i][0] = Grid[i-1][0]+indelPenalty

for i in range(1,m+1):
    for j in range(1,n+1):
        l = [indelPenalty+Grid[i][j-1],indelPenalty+Grid[i-1][j],BLOSUM62[(word2[i-1],word1[j-1])] + Grid[i-1][j-1],]
        Grid[i][j] = max(l)
        BestWayToReach[i][j] = l.index(max(l))

i,j = m,n
L = []
print(n,m)
while BestWayToReach[i][j] != -1:
    L.append((j,i))
    idx = BestWayToReach[i][j]
    if idx == 2:
        #print(word1[j-1],word2[i-1],end="",sep="")
        i -= 1
        j -= 1
    elif idx == 1:
        #print("-",word2[i-1],end="",sep="")
        i -= 1
    elif idx == 0:
        #print(word1[j-1],"-",end="",sep="")
        j -= 1

x = int(len(L)/2)

print(L[x+1],L[x])
print(L[x],L[x-1])